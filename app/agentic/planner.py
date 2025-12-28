import json
from app.agentic.schemas import ReasoningTask
from app.agentic.prompt import TASK_DECOMPOSITION_PROMPT
from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL


class TaskPlanner:
    """
    Converts a user request into a small, bounded reasoning plan.
    """

    def plan(self, user_message: str) -> list[ReasoningTask]:
        prompt = TASK_DECOMPOSITION_PROMPT.format(user_message=user_message)

        raw = call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.0)

        try:
            start = raw.find("{")
            end = raw.find("}")
            data = json.loads(raw[start : end + 1])

            return [ReasoningTask(**t) for t in data["tasks"]]

        except Exception:
            return [
                ReasoningTask(description="Answer the user's question", tool="none")
            ]
