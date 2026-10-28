import os

from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# List models available through the API
for model in client.models.list():
    if model.supported_actions and "generateContent" in model.supported_actions:
        print(model.name)
