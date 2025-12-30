from fastapi import APIRouter, UploadFile, File, Form
from uuid import uuid4
from app.api.models import ChatResponse
from app.core.orchestrator import Orchestrator
from app.memory.store import get_session
from app.memory.manager import get_conversation_context
from app.ingestion.router import ingest_file
from app.utils.token_counter import estimate_tokens

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    message: str = Form(...),
    session_id: str = Form(...),
    file: UploadFile | None = File(None),
):
    request_id = str(uuid4())
    session = get_session(session_id)
    file_attached_in_request = False

    if file is not None:
        document_id = ingest_file(file)
        if session.document_ids is None:
            session.document_ids = [document_id]
        else:
            session.document_ids.append(document_id)
        file_attached_in_request = True

    answer = Orchestrator().handle(
        user_message=message,
        request_id=request_id,
        session_id=session_id,
        file_attached_in_request=file_attached_in_request,
    )

    return ChatResponse(request_id=request_id, answer=answer)


@router.get("/debug/session/{session_id}")
def debug_session(session_id: str):
    """
    Debug endpoint to inspect session state and conversation context.
    """
    session = get_session(session_id)
    conversation_context = get_conversation_context(session_id)

    # Calculate token counts
    total_turn_tokens = sum(estimate_tokens(turn.content) for turn in session.turns)
    context_tokens = estimate_tokens(conversation_context)
    summary_tokens = estimate_tokens(session.summary) if session.summary else 0

    return {
        "session_id": session_id,
        "summary": session.summary,
        "summary_tokens": summary_tokens,
        "turn_count": len(session.turns),
        "total_turn_tokens": total_turn_tokens,
        "turns": [
            {
                "role": turn.role,
                "content": (
                    turn.content[:200] + "..."
                    if len(turn.content) > 200
                    else turn.content
                ),
                "tokens": estimate_tokens(turn.content),
            }
            for turn in session.turns
        ],
        "document_ids": session.document_ids,
        "conversation_context": conversation_context,
        "conversation_context_length": len(conversation_context),
        "conversation_context_tokens": context_tokens,
    }
