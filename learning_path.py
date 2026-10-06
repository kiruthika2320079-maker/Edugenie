from gemini_client import generate

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""Create a personalized learning path for the topic below.
Organize it from beginner to advanced.
Include stages, suggested practice, and useful types of resources.

Topic:
{topic}
"""
    return generate(prompt)
