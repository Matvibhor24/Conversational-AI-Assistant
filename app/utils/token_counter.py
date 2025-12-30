"""
Utility for counting tokens in text using tiktoken.
"""

import tiktoken
from typing import Optional


# Cache the encoder to avoid reloading it
_encoder: Optional[tiktoken.Encoding] = None


def get_encoder() -> tiktoken.Encoding:
    """Get or create the tiktoken encoder."""
    global _encoder
    if _encoder is None:
        # Use cl100k_base which is compatible with GPT-4 and most OpenAI models
        # This is a reasonable approximation for Gemini as well
        _encoder = tiktoken.get_encoding("cl100k_base")
    return _encoder


def count_tokens(text: str) -> int:
    """
    Count the number of tokens in a text string.

    Args:
        text: The text to count tokens for

    Returns:
        The number of tokens
    """
    if not text:
        return 0
    encoder = get_encoder()
    return len(encoder.encode(text))


def estimate_tokens(text: str) -> int:
    """
    Estimate tokens using a simple character-based approximation.
    This is faster but less accurate than count_tokens.
    Uses ~4 characters per token as a rough estimate.

    Args:
        text: The text to estimate tokens for

    Returns:
        Estimated number of tokens
    """
    if not text:
        return 0
    return len(text) // 4
