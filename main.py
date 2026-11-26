
# CT PROJECT - HUMILITY.AI

from google import genai
from google.genai import types
import os


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# CONVERSATION HISTORY SECTION
conversation_history = []

def chat_with_gemini(prompt):

    history_length = len(conversation_history)

    try:

        # SAVE USER MESSAGE
        conversation_history.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)]
            )
        )

        # GENERATE AI RESPONSE
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation_history
        )

        if response.text:

            bot_reply = response.text.strip()

            # SAVE AI RESPONSE
            conversation_history.append(
                types.Content(
                    role="model",
                    parts=[types.Part.from_text(text=bot_reply)]
                )
            )

            return bot_reply

        else:
            conversation_history.pop()
            return "Sorry, I am unable to generate a response."

    # ERROR HANDLING SECTION
    except Exception as e:

        print("ERROR TYPE:", type(e).__name__)
        print("ERROR DETAILS:", repr(e))

        del conversation_history[history_length:]

        return "Sorry, something went wrong. Please try again."


# MAIN FUNCTION
if __name__ == "__main__":

    while True:

        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Humility.AI: Goodbye!")
            break

        response = chat_with_gemini(user_input)

        print("Humility.AI:", response)
