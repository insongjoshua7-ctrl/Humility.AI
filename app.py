
# CT PROJECT - HUMILITY.AI
# WEBSITE INTERFACE

import streamlit as st
from main import chat_with_gemini

# WEBSITE CONFIGURATION
st.set_page_config(
    page_title="Humility.AI",
    page_icon="🤖",
    layout="centered"
)

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

    # SAVE USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # DISPLAY USER MESSAGE
    with st.chat_message("user"):
        st.write(user_prompt)

    # GENERATE AI RESPONSE
    with st.chat_message("assistant"):

        with st.spinner("Humility.AI is thinking..."):

            bot_reply = chat_with_gemini(
                st.session_state.messages
            )

            st.write(bot_reply)

    # SAVE AI RESPONSE
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })
