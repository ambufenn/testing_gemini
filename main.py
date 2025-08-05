import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

print("🤖 Gemini Chatbot. Ketik 'exit' untuk keluar.")

while True:
    user_input = input("Kamu: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
