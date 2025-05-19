import os
import hashlib
import json
from functools import lru_cache
from typing import Any

import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "")


@lru_cache(maxsize=32)
def call_openai(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Call OpenAI API with simple caching."""
    if not openai.api_key:
        return "OpenAI API key not configured."
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

