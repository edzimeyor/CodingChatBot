from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

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

st.set_page_config(
    page_title="AI Python Tutor",
    page_icon="🤖",
    layout="centered"
)
st.title("AI Python Tutor")

st.write("Welcome to the AI Python Tutor! Ask me anything about Python programming, "
         "and I'll do my best to help you learn. You can also share code snippets, "
         "and I'll provide feedback on them."
)

# Initialize chat history
if "conversation" not in st.session_state:

    st.session_state.conversation = [
        {"role": "system", "content": system_prompt}
    ]

# Display previous messages
for message in st.session_state.conversation:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])

    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your Python question here...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Detect code snippets
    code_keywords = ["def", "print", "for", "while", "if", "else", "elif", "="]

    if any(keyword in user_input for keyword in code_keywords):

        st.session_state.conversation.append({
            "role": "system",
            "content": "The user may provide Python code. "
                       "Provide debugging help if needed."
        })

    st.session_state.conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.conversation,
        temperature=0.7
    )

    tutor_reply = response.choices[0].message.content

    # Display response
    with st.chat_message("assistant"):
        st.markdown(tutor_reply)

    st.session_state.conversation.append({
        "role": "assistant",
        "content": tutor_reply
    })