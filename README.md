
# Gemini Calculator AI Agent

A conversational AI calculator built using Python and Google's Gemini API.

This project demonstrates the fundamentals of Agentic AI, including LLM integration, function calling, tool execution, and conversation history.

## Features

- Natural-language calculations
- Addition, subtraction, multiplication, and division
- Gemini-powered tool selection
- Multi-step mathematical calculations
- Conversational follow-up questions
- Interactive command-line interface
- Secure API key management using environment variables

## Technologies

- Python 3.11
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- Git and GitHub

## How It Works

1. The user enters a calculation request.
2. Gemini interprets the request.
3. Gemini selects an appropriate Python calculator function.
4. The SDK executes the function and returns its result.
5. Gemini generates a natural-language response.
6. The conversation continues until the user types `exit`.

## Project Structure

```text
my-first-agent/
├── agent.py
├── check_models.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `.env` file is created locally and is excluded from Git.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abdulwakeel12/my-first-agent.git
cd my-first-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit your actual API key.

### 5. Run the agent

```bash
python agent.py
```

## Example

```text
You: What is 100 multiplied by 25?
Gemini: 100 multiplied by 25 is 2500.

You: Now divide that result by 5.
Gemini: Dividing 2500 by 5 gives 500.

You: exit
```

## Architecture

User → Gemini LLM → Python Calculator Tools → Gemini Response

The Gemini SDK handles automatic function calling, while Python performs the calculations.

## Future Improvements

- Better error handling
- Persistent conversation history
- Tool execution logging
- Automated tests
- Additional mathematical operations

## Project Status

Completed — First Agentic AI learning project.
