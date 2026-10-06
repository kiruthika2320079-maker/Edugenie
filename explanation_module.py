from gemini_client import generate

def explain_topic(topic: str) -> str:
    prompt = f"""Explain the following topic for a beginner.
Give a simple definition, 3-5 key points, and one easy example.
Avoid unnecessary jargon.

Topic:
{topic}
"""
    return generate(prompt)
