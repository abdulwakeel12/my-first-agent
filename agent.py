import os

from dotenv import load_dotenv
from google import genai

# Step 1: Define calculator tools

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Divide a by b and return the result. Do not divide by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Step 2: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# Step 3: Create Gemini client
client = genai.Client(api_key=api_key)


# Step 4: Register calculator tools
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={
        "tools": [
            add_numbers,
            subtract_numbers,
            multiply_numbers,
            divide_numbers
        ]
    }
)


# Step 5: Start a conversation loop
while True:

    # Get the user's question
    user_question = input("🧑 You: ")

    # Exit when the user types "exit"
    if user_question.lower().strip() == "exit":
        break

    # Send the question to Gemini
    response = chat.send_message(user_question)

    # Display Gemini's answer
    print("🤖 Gemini:", response.text)