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
        self,
        user_message: str,
        conversation_context: str | None = None,
        attachments: list[str] | None = None,
    ) -> Understanding:
        attachment_text = (
            "\n".join(f"- {a}" for a in attachments) if attachments else "None"
        )
        prompt = UNDERSTANDING_PROMPT_TEMPLATE.format(
            user_message=user_message,
            conversation_context=conversation_context or "None",
            attachments=attachment_text,
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
                clarity="ambiguous",
                clarification_question="Could you clarify what you are referring to?",
                attachment_use="ignore",
                attachment_scope="none",
                response_depth="short",
                reasoning_complexity="simple",
                tool_requirements="none",
                confidence=0.3,
            )
