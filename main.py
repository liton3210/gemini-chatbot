import os
from google import genai
from google.genai import errors
from dotenv import load_dotenv

MODEL_NAME = "gemini-3.6-flash"

class Geminichatbot:
    """A chat bot that remember the whole convversation."""
    def __init__ (self, api_key: str, model_name: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.chat = self.client.chats.create(model=model_name)

    def reply(self, question: str) -> str:
        try:
            response = self.chat.send_message(question)
        except errors.APIError as e:
            return(f"\nSorry, something went wrong, (code: {e.code}), please try again.")
        return response.text or ""


def main() -> None:
    """Start the chat bot."""
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("\nGEMINI_API_KEY is missing, please add it to your .env file.")

    bot = Geminichatbot(api_key, MODEL_NAME)
    print("\nServer is ready >>> ")

    while True:
        question = input("\nAsk question: ")
        print("\nType exit or quit to close the conversation.")
        if question.strip() in {"exit", "quit"}:
            print("\nGoodbye!")
            break
        
        print("\nBot: ", bot.reply(question))
        print("~"*50)

if __name__ == "__main__":
    main()