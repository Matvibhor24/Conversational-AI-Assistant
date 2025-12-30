from pydantic import BaseModel


class ChatResponse(BaseModel):
    request_id: str
    answer: str
