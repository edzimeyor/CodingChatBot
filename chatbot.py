from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("chatkey"))

system_prompt = """
You are a beginner-friendly Python tutor.
Always respond using this format:

1. Concept Explanation
2. Code Example
3. Practice Exercise
4. Feedback
"""

conversation = [
    {"role": "system", "content": system_prompt}
]

while True:

    user_input = input("Student: ")

    if user_input.lower() == "quit":
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7
    )

    tutor_reply = response.choices[0].message.content

    print("\nTutor:\n")
    print(tutor_reply)

    conversation.append({
        "role": "assistant",
        "content": tutor_reply
    })