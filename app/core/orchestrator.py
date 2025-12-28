from app.schemas import understanding
from app.understanding.engine import UnderstandingEngine
from app.core.router import ModeRouter
from app.schemas.response import RoutedResponse
from app.conversation.responder import DirectResponder
from app.agentic.planner import TaskPlanner
from app.agentic.executor import ToolExecutor
from app.agentic.verifier import AnswerSynthesizer
from app.utils.logging import log_event
from app.memory.store import add_turn, get_session
from app.memory.manager import update_memory


class Orchestrator:
    """
    High level controller for a single user request.
    """

    def handle(
        self, user_message: str, request_id: str, session_id: str
    ) -> RoutedResponse:
        session = get_session(session_id)
        memory_context = session.summary
        log_event(
            "request_received",
            {"message_preview": user_message[:100]},
            request_id,
        )
        understanding = UnderstandingEngine().analyze(
            user_message=user_message, memory_context=memory_context
        )

        log_event(
            "understanding_complete",
            {
                "clarity": understanding.clarity,
                "response_depth": understanding.response_depth,
                "tool_requirements": understanding.tool_requirements,
                "confidence": understanding.confidence,
            },
            request_id,
        )
        route = ModeRouter().route(understanding)

        log_event("route_selected", {"mode": route.mode}, request_id)

        if route.mode == "clarification":
            add_turn(session_id, "assistant", route.message)
            log_event("response_type", {"type": "clarification"}, request_id)
            return route.message
        if route.mode == "direct":
            response = DirectResponder().respond(
                user_message=user_message, understanding=understanding
            )
            add_turn(session_id, "user", user_message)
            add_turn(session_id, "assistant", response)
            update_memory(session_id)
            log_event("response_type", {"type": "direct"}, request_id)
            return response

        if route.mode == "deep":
            tasks = TaskPlanner().plan(user_message)
            log_event(
                "deep_tasks_planned",
                {"task_count": len(tasks), "tools": [t.tool for t in tasks]},
                request_id,
            )
            results = ToolExecutor().execute(tasks, user_message)
            response = AnswerSynthesizer().synthesize(user_message, results)

            log_event("response_type", {"type": "deep"}, request_id)

            return response

        return "Deep reasoning path not implemented yet."
