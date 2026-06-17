import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GROQ_API_KEY"))

model = genai.GenerativeModel("openai/gpt-oss-20b")

response = model.generate_content("Hello")

print(response.text)
