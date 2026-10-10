from langchain_ollama import ChatOllama
from tabulate import tabulate

llm = ChatOllama(model="qwen2.5:1.5b", temperature=0)

prompt = (
    "Give me exactly 5 healthy breakfast ideas.\n"
    "Rules:\n"
    "- Exactly 5 lines, each on its own line.\n"
    "- Each line: dish name | main ingredients | why it's healthy\n"
    "- Use the | symbol between the three parts.\n"
    "- No numbering, no header, no preamble, no closing text."
)

response = llm.invoke(prompt)

rows = []
for line in response.content.strip().splitlines():
    parts = [p.strip() for p in line.split("|")]
    if len(parts) == 3:  # skip any broken line
        rows.append(parts)

print(tabulate(rows, headers=["Dish", "Ingredients", "Why healthy"], tablefmt="grid"))