from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


def synthesize_summary(chunk_summaries: list[str]) -> str:
    joined = "\n".join(chunk_summaries)

    prompt = f"""
    You are given summaries of different parts of a document.
    Produce a coherent overall summary.

    Guidelines:
    - Cover all main themes
    - Be concise
    - Avoid repetition
    - Do NOT add new information

    Summaries:
    {joined}
    """
    return call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.2).strip()
