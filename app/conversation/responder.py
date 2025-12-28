from app.tools.llm import call_llm
from app.conversation.prompt import DIRECT_RESPONSE_PROMPT
from app.schemas.understanding import Understanding
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


class DirectResponder:
    """
    Handles cheap, conversational responses.
    """

    def respond(self, user_message: str, understanding: Understanding) -> str:
        prompt = DIRECT_RESPONSE_PROMPT.format(
            user_message=user_message, response_depth=understanding.response_depth
        )

        response = call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.3)
        return response.strip()
