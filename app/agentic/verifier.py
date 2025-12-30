from app.tools.llm import call_llm
from app.config.constants import GEMINI_MODEL, OPENAI_MODEL
from app.memory.store import get_session
from app.agentic.global_document import generate_global_summary
from app.documents.store import get_document


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

    def from_document_summary(
        self, user_message: str, session_id: str, conversation_context: str
    ) -> str:
        session = get_session(session_id)
        document_id = session.document_ids[-1]
        document = get_document(document_id)
        if not document.has_summary:
            summary = generate_global_summary(document)
        summary = document.summary
        prompt = f"""
        Answer the user's question using the following document summary.

        {conversation_context}

        Document Summary:
        {summary}

        User Question:
        {user_message}
        """

        return call_llm(model=OPENAI_MODEL, prompt=prompt, temperature=0.2)
