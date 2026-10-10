# Healthy Breakfast Ideas (LangChain + Ollama)

A small Python script that asks a local AI model for 5 healthy breakfast ideas and prints them as a table.

It runs fully on your computer. No API key. No internet needed after setup.

## What it uses

- Python 3.9 or higher
- [LangChain](https://python.langchain.com/) (`langchain-ollama`)
- [Ollama](https://ollama.com/) to run the model locally
- Qwen 2.5 (1.5b) as the model
- `tabulate` to print the table

## Setup

1. Install Ollama from https://ollama.com/ and make sure it is running.

2. Download the model:

   ```bash
   ollama pull qwen2.5:1.5b
   ```

3. Install the Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Run

```bash
python breakfast_ideas.py
```

## Example output

```
+--------------------------+-------------------------------+----------------------------------+
| Dish                     | Ingredients                   | Why healthy                      |
+==========================+===============================+==================================+
| Greek Yogurt Bowl        | Greek yogurt, berries, almonds| High in protein and antioxidants |
+--------------------------+-------------------------------+----------------------------------+
| ...                      | ...                           | ...                              |
+--------------------------+-------------------------------+----------------------------------+
```

Your results will differ. The model gives slightly different ideas each time.

## How it works

1. The script sends a clear prompt to the model: exactly 5 ideas, one per line, parts separated by `|`, no extra text.
2. `llm.invoke()` returns a message object, not plain text. The text is in `response.content`.
3. Python splits each line on `|` and builds the table. Any broken line is skipped.

## Tips

- **Fewer than 5 rows?** The small model sometimes breaks the format. Run it again.
- **Same output every time:** keep `temperature=0` in the script.
- **Better quality:** try a bigger model, for example `ollama pull qwen2.5:7b`, then change the model name in the script.
- **Markdown table:** change `tablefmt="grid"` to `tablefmt="github"`.

## Project files

```
.
├── breakfast_ideas.py   # the script
├── requirements.txt     # Python packages
└── README.md            # this file
```

## requirements.txt

```
langchain-ollama
tabulate
```

## License

MIT
