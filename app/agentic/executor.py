from app.agentic.schemas import ReasoningTask
from app.tools.summarizer import summarize_text


class ToolExecutor:
    """
    Executes reasoning tasks in a bounded manner.
    """

    def execute(self, tasks: list[ReasoningTask], user_message: str) -> list[str]:
        results = []
        for task in tasks:
            if task.tool == "summarize":
                results.append(summarize_text(user_message))
            else:
                results.append(task.description)
        return results
