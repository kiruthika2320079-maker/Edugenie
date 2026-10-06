import json
from gemini_client import generate

def _clean_json(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text

def generate_quiz(topic_or_text: str) -> str:
    prompt = f"""Create exactly 3 multiple-choice questions from the material below.
Each question must have exactly 4 options and one correct answer.
Return ONLY valid JSON in this format:
[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Material:
{topic_or_text}
"""
    raw = _clean_json(generate(prompt))
    try:
        data = json.loads(raw)
        if not isinstance(data, list) or len(data) != 3:
            raise ValueError("Quiz response did not contain exactly 3 questions.")
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Invalid quiz item.")
            if len(item.get("options", [])) != 4:
                raise ValueError("Each quiz question must have 4 options.")
            if item.get("answer") not in item["options"]:
                raise ValueError("Quiz answer is not one of the options.")
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as exc:
        raise RuntimeError(f"Quiz parsing failed. Please try again. Details: {exc}") from exc
