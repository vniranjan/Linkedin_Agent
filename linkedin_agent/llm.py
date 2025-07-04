import os
from typing import Optional

import openai


openai.api_key = os.environ.get("OPENAI_API_KEY")


def chat_completion(prompt: str, *, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> str:
    """Call OpenAI Chat API and return the assistant message."""
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set")

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    return response["choices"][0]["message"]["content"].strip()
