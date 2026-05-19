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
4. Feedback(only if code snippet is provided)
"""

conversation = [
    {"role": "system", "content": system_prompt}
]

while True:

    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit", "bye", "end", "stop"]:
        break

    if user_input.lower() in ["def", "print", "for", "while", "if", "else", "elif"]:
        conversation.append({
            "role": "system",
            "content": "the following will be a code snippet:"
        })

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