from app.memory.store import get_session
from app.memory.summarizer import summarize_session

MAX_TURNS = 6


def update_memory(session_id: str):
    session = get_session(session_id)

    if len(session.turns) > MAX_TURNS:
        session.summary = summarize_session(session)
        session.turns = session.turns[-2:]
