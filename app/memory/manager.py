from app.memory.store import get_session
from app.memory.summarizer import summarize_session
from app.utils.token_counter import count_tokens, estimate_tokens
from app.config.constants import (
    MAX_CONTEXT_TOKENS,
    MAX_TURNS_BEFORE_SUMMARY,
    MIN_TURNS_TO_KEEP,
)


def update_memory(session_id: str):
    """
    Update memory by summarizing old conversation if needed.
    Triggers summarization based on both turn count and token count.
    """
    session = get_session(session_id)

    # Check if we need to summarize based on turn count
    should_summarize_by_turns = len(session.turns) > MAX_TURNS_BEFORE_SUMMARY

    # Check if we need to summarize based on token count
    # Count tokens in all turns
    total_tokens = 0
    for turn in session.turns:
        total_tokens += estimate_tokens(turn.content)

    # If we have a summary, check if adding recent turns would exceed limit
    if session.summary:
        summary_tokens = estimate_tokens(session.summary)
        recent_tokens = sum(
            estimate_tokens(turn.content) for turn in session.turns[-MIN_TURNS_TO_KEEP:]
        )
        should_summarize_by_tokens = (
            summary_tokens + recent_tokens
        ) > MAX_CONTEXT_TOKENS
    else:
        # If no summary yet, check if total tokens exceed threshold
        should_summarize_by_tokens = total_tokens > MAX_CONTEXT_TOKENS * 1.5

    if should_summarize_by_turns or should_summarize_by_tokens:
        # Summarize all current turns
        session.summary = summarize_session(session)
        # Keep only the most recent turns
        session.turns = session.turns[-MIN_TURNS_TO_KEEP:]


def get_conversation_context(
    session_id: str, max_tokens: int = MAX_CONTEXT_TOKENS
) -> str:
    """
    Get conversation context with token-aware truncation.

    Args:
        session_id: The session ID
        max_tokens: Maximum tokens to include in context

    Returns:
        Formatted conversation context string
    """
    session = get_session(session_id)

    parts = []
    current_tokens = 0

    # 1. Always include summary if exists (it's already condensed)
    if session.summary:
        summary_text = f"Conversation summary:\n{session.summary}"
        summary_tokens = estimate_tokens(summary_text)
        if summary_tokens <= max_tokens:
            parts.append(summary_text)
            current_tokens += summary_tokens
        else:
            # If summary itself is too long, truncate it
            # This shouldn't happen often, but handle it gracefully
            truncated_summary = session.summary[: max_tokens * 4]  # Rough char estimate
            parts.append(f"Conversation summary:\n{truncated_summary}...")
            current_tokens = max_tokens  # Set to max to prevent adding more

    # 2. Include recent turns up to token limit
    remaining_tokens = max_tokens - current_tokens
    if remaining_tokens > 100:  # Only add turns if we have meaningful space
        recent_turns_text = []
        turns_tokens = 0

        # Add turns from most recent to oldest until we hit token limit
        for turn in reversed(session.turns):
            turn_text = f"{turn.role.capitalize()}: {turn.content}"
            turn_tokens = estimate_tokens(turn_text)

            if turns_tokens + turn_tokens <= remaining_tokens:
                recent_turns_text.insert(
                    0, turn_text
                )  # Insert at beginning to maintain order
                turns_tokens += turn_tokens
            else:
                # If this turn would exceed limit, try to include a truncated version
                # Only if we haven't added any turns yet (to ensure at least one recent turn)
                if not recent_turns_text:
                    # Truncate the turn content to fit
                    available_chars = (remaining_tokens - turns_tokens) * 4
                    truncated_content = turn.content[:available_chars]
                    recent_turns_text.insert(
                        0, f"{turn.role.capitalize()}: {truncated_content}..."
                    )
                break

        if recent_turns_text:
            parts.append("Recent conversation:")
            parts.extend(recent_turns_text)

    return "\n".join(parts) if parts else "(empty)"
