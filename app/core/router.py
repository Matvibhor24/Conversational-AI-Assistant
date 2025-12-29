from app.schemas.understanding import Understanding
from app.schemas.response import RoutedResponse


class ModeRouter:
    """
    Maps understanding to high-level execution nodes.
    """

    def route(self, understanding: Understanding) -> RoutedResponse:
        # 1: Ambiguity -> clarification
        if understanding.clarity == "ambiguous":
            return RoutedResponse(
                mode="clarification", message=understanding.clarification_question
            )

        # 2. Simple + no attachment + no tools → direct
        if (
            understanding.reasoning_complexity == "simple"
            and understanding.attachment_use == "ignore"
            and understanding.tool_requirements == "none"
        ):
            return RoutedResponse(mode="direct")

        # Rule3: Deep response requested -> deep reasoning
        # if understanding.response_depth == "deep":
        #     return RoutedResponse(mode="deep")

        # # Rule4: Default -> direct response
        # return RoutedResponse(mode="direct")
        return RoutedResponse(mode="deep")
