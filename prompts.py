def explain_prompt(code):
    return f"Explain what this Python code does:\n\n```python\n{code}\n```"

def refactor_prompt(code):
    return f"Refactor this Python code for better readability and performance:\n\n```python\n{code}\n```"

def docstring_prompt(code):
    return f"Add or improve the docstrings in this Python code:\n\n```python\n{code}\n```"
