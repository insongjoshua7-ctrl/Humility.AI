
import streamlit as st
from google import genai
import os

# WEBSITE CONFIGURATION
st.set_page_config(
    page_title="Humility.AI",
    page_icon="🤖",
    layout="centered"
)

# GEMINI CONFIGURATION
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found!")
    st.stop()

client = genai.Client(api_key=api_key)
SYSTEM_INSTRUCTION = """
You are Humility.AI, an AI chatbot created by its developer.

Your name is Humility.AI, NOT Gemini.

If someone asks for your name, introduce yourself as Humility.AI.

You are helpful, respectful, friendly, and informative.

Never claim that your name is Gemini.
"""

MODEL = "gemini-3.5-flash-lite"

# WEBSITE TITLE
st.title("🤖 Humility.AI")
st.caption("Your AI-powered conversation assistant.")

# CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = []

# DISPLAY CHAT HISTORY
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# USER INPUT
user_prompt = st.chat_input("Message Humility.AI...")

if user_prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.write(user_prompt)

    # GEMINI RESPONSE
    with st.chat_message("assistant"):

        with st.spinner("Humility.AI is thinking..."):

            try:
                response = client.models.generate_content(
                     model=MODEL,
                     contents=user_prompt,
                     config={
                     "system_instruction": SYSTEM_INSTRUCTION
                    }
                )

                bot_reply = response.text

                st.write(bot_reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

            except Exception as e:
                st.error(f"An error occurred: {e}")
