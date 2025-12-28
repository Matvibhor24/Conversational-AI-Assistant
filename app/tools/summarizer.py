from app.tools.llm import call_llm
from app.config.constants import OPENAI_MODEL, GEMINI_MODEL


def summarize_text(text: str) -> str:
    """
    Summarizes the given text.
    Used ONLY in deep reasoning mode.
    """

    prompt = f"""
Summarize the following content clearly and concisely.

Guidelines:
- Capture the main idea
- Keep it factual
- Do not add new information

Content:
{text}
"""

    summary = call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.2)

    return summary.strip()
