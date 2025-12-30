from app.memory.store import get_session
from app.memory.summarizer import summarize_session

MAX_TURNS = 6


def update_memory(session_id: str):
    session = get_session(session_id)

    if len(session.turns) > MAX_TURNS:
        session.summary = summarize_session(session)
        session.turns = session.turns[-2:]


def get_conversation_context(session_id: str, last_n: int = 4) -> str:
    session = get_session(session_id)

    parts = []

    # 1. Include summary if exists
    if session.summary:
        parts.append(f"Conversation summary:\n{session.summary}")

    # 2. Include last N turns
    recent_turns = session.turns[-last_n:]
    if recent_turns:
        parts.append("Recent conversation:")
        for turn in recent_turns:
            parts.append(f"{turn.role.capitalize()}: {turn.content}")

    return "\n".join(parts)
