import argparse
from llm_local import call_local_llm
from prompts import explain_prompt, refactor_prompt, docstring_prompt
from rich import print

def load_code(path):
    with open(path, 'r') as file:
        return file.read()

parser = argparse.ArgumentParser(description="AI Code Assistant (Local LLM)")
parser.add_argument("file", help="Path to the Python code file")
parser.add_argument("mode", choices=["explain", "refactor", "doc"], help="Action to perform")

args = parser.parse_args()

code = load_code(args.file)

if args.mode == "explain":
    prompt = explain_prompt(code)
elif args.mode == "refactor":
    prompt = refactor_prompt(code)
else:
    prompt = docstring_prompt(code)

response = call_local_llm(prompt)
print("\n[bold green]--- AI Response ---[/bold green]\n")
print(response)
