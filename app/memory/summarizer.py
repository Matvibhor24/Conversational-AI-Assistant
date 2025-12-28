from app.memory import session
from app.tools.llm import call_llm
from app.memory.session import SessionMemory
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


def summarize_session(session: SessionMemory) -> str:
    transcript = "\n".join(f"{t.role}: {t.content}" for t in session.turns)

    prompt = f"""
    Summarize the following conversation briefly.
    Focus on key context and decisions.

    Conversation:
    {transcript}
    """

    return call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.3)
