from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def call_llm(model: str, prompt: str, temperature: float = 0.0) -> str:
    if model.startswith("gpt"):
        client = openai_client
    elif model.startswith("gemini"):
        client = gemini_client
    else:
        # Default to OpenAI if model type is unclear
        client = openai_client
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a precise JSON generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()
