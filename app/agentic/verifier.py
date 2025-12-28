from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


class AnswerSynthesizer:
    """
    Synthesizes final answer from tool outputs.
    """

    def synthesize(self, user_message: str, results: list[str]) -> str:
        prompt = f"""
        User Question:
        "{user_message}"

        Intermediate results:
        {results}

        Produce a clear, helpful final answer.
        """

        return call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.2)
