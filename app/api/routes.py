from fastapi import APIRouter
from uuid import uuid4
from app.api.models import ChatRequest, ChatResponse
from app.core.orchestrator import Orchestrator

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    request_id = str(uuid4())

    answer = Orchestrator().handle(user_message=request.message, request_id=request_id)

    return ChatResponse(request_id=request_id, answer=answer)
