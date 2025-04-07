# AI Code Assistant

A local AI-powered code assistant that helps you understand, refactor, and document Python code using a local LLM (Large Language Model).

## Features

- **Code Explanation**: Get detailed explanations of Python code
- **Code Refactoring**: Improve code readability and performance
- **Documentation**: Add or improve docstrings in your code

## Prerequisites

- Python 3.x
- Ollama (for running local LLM)
- Required Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-code-assistant
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure you have Ollama installed and running locally with the CodeLlama model:
```bash
ollama pull codellama
```

## Usage

The AI Code Assistant can be used in three different modes:

1. **Explain Code**:
```bash
python main.py your_code.py explain
```

2. **Refactor Code**:
```bash
python main.py your_code.py refactor
```

3. **Add Documentation**:
```bash
python main.py your_code.py doc
```

## How It Works

The tool uses a local LLM (CodeLlama by default) to analyze and process your Python code. It sends the code to the LLM with specific prompts based on the selected mode and returns the AI's response.

## Configuration

By default, the tool uses the following settings:
- LLM Model: CodeLlama
- Local API URL: http://localhost:11434/api/generate

You can modify these settings in the `llm_local.py` file if needed.

## Requirements

- requests
- rich
