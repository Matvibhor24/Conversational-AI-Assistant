from typing import Dict
from app.memory.session import SessionMemory, Turn

_MEMORY: Dict[str, SessionMemory] = {}


def get_session(session_id: str) -> SessionMemory:
    if session_id not in _MEMORY:
        _MEMORY[session_id] = SessionMemory(session_id=session_id, turns=[])
    return _MEMORY[session_id]


def add_turn(session_id: str, role: str, content: str):
    session = get_session(session_id)
    session.turns.append(Turn(role=role, content=content))
