from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


def summarize_chunk(chunk: str) -> str:
    prompt = f"""
    Summarize the following part of a document.
    Guidelines:
    - Keep it concise.
    - Preserve key facts.
    - Do not add new information.

    Text:
    {chunk}
    """

    return call_llm(MODEL=OPENAI_MODEL, prompt=prompt, temperature=0.2).strip()
