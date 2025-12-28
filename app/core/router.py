from app.schemas.understanding import Understanding
from app.schemas.response import RoutedResponse


class ModeRouter:
    """
    Decides how the system should respond based on understanding metadata.
    """

    def route(self, understanding: Understanding) -> RoutedResponse:
        # Rule1: Ambiguity -> clarification
        if understanding.clarity == "ambiguous":
            return RoutedResponse(
                mode="clarification", message=understanding.clarification_question
            )
        # Rule2: Required tools -> deep reasoning
        if understanding.tool_requirements == "required":
            return RoutedResponse(mode="deep")

        # Rule3: Deep response requested -> deep reasoning
        if understanding.response_depth == "deep":
            return RoutedResponse(mode="deep")

        # Rule4: Default -> direct response
        return RoutedResponse(mode="direct")
