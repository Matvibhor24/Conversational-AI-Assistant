from fastapi import APIRouter
from uuid import uuid4
from app.api.models import ChatRequest, ChatResponse
from app.core.orchestrator import Orchestrator
from app.memory.store import get_session
from app.ingestion.router import ingest_file

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    request_id = str(uuid4())
    session = get_session(request.session_id)
    file_attached_in_request = False

    if request.file is not None:
        document_id = ingest_file(request.file)
        session.document_id = document_id
        file_attached_in_request = True

    answer = Orchestrator().handle(
        user_message=request.message,
        request_id=request_id,
        session_id=request.session_id,
        file_attached_in_request=file_attached_in_request,
    )

    return ChatResponse(request_id=request_id, answer=answer)
