UNDERSTANDING_PROMPT_TEMPLATE = """
You are an understanding engine for a general purpose AI assistant.

Your task is to understand the user's request.
You must not answer the user.

User message:
"{user_message}"

Return ONLY valid JSON in this exact schema:

{{
    "user_goal": "<string>",
    "clarity": "clear | ambiguous",
    "clarification_question": "<string or null>",
    "response_depth": "short | medium | deep",
    "tool_requirements": "none | optional | required",
    "confidence": <decimal between 0 and 1>
}}

Rules:
- If the request refers to something unspecified (eg. "this", "that", "it"), mark clarity as "ambiguous".
- If ambiguous, propose ONE short clarification question.
- Choose response_depth based on how much explanation is appropriate.
- Set tool_requirements to "required" ONLY if tools or external context are necessary.
- Do NOT include explanations.
- Do NOT include extra keys.
"""
