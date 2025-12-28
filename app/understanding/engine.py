import json
from app.schemas.understanding import Understanding
from app.understanding.prompt import UNDERSTANDING_PROMPT_TEMPLATE
from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


class UnderstandingEngine:
    """
    Uses a cheap LLM call to understand the user's request.
    Produces metadata, not answers.
    """

    def analyze(
        self, user_message: str, memory_context: str | None = None
    ) -> Understanding:
        context_block = (
            f'\nConversation summary: \n"{memory_context}"' if memory_context else ""
        )
        prompt = UNDERSTANDING_PROMPT_TEMPLATE.format(
            user_message=user_message + context_block
        )

        raw_output = call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.0)

        # print("RAW LLM OUTPUT:")
        # print(raw_output)

        try:
            # Extract JSON from markdown code blocks if present
            json_content = raw_output.strip()
            if json_content.startswith("```"):
                # Remove markdown code block markers (```json or ```)
                lines = json_content.split("\n")
                # Remove first line (```json) and last line (```)
                json_content = "\n".join(lines[1:-1])

            parsed = json.loads(json_content)
            return Understanding(**parsed)

        except Exception as e:
            print(f"ERROR parsing LLM output: {e}")
            return Understanding(
                user_goal="unknown",
                clarity="ambiguous",
                clarification_question="Could you clarify what you are referring to?",
                response_depth="short",
                tool_requirements="none",
                confidence=0.3,
            )
