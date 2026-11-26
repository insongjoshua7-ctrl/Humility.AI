
# CT PROJECT - HUMILITY.AI
# MAIN AI ENGINE

from google import genai
from google.genai import types
import streamlit as st
import os

# API CONFIGURATION
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        raise RuntimeError("Gemini API key not found.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"

SYSTEM_INSTRUCTION = """
You are Humility.AI, an AI chatbot created by its developer.

Your name is Humility.AI, NOT Gemini.

If someone asks for your name, introduce yourself as Humility.AI.

You are helpful, respectful, friendly, and informative.

Never claim that your name is Gemini.
"""


# AI RESPONSE FUNCTION
def chat_with_gemini(messages):

    try:

        # CONVERT CHAT HISTORY
        conversation = []

        for message in messages:

            role = message["role"]

            if role == "assistant":
                role = "model"

            conversation.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part.from_text(
                            text=message["content"]
                        )
                    ]
                )
            )

        # GENERATE RESPONSE
        response = client.models.generate_content(
            model=MODEL,
            contents=conversation,
            config={
                "system_instruction": SYSTEM_INSTRUCTION
            }
        )

        if response.text:
            return response.text.strip()

        return "Sorry, I am unable to generate a response."

    except Exception as e:

        print("ERROR TYPE:", type(e).__name__)
        print("ERROR DETAILS:", repr(e))

        return "Sorry, something went wrong. Please try again."
