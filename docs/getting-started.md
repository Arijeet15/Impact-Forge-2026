# Getting Started

Beyond Blocks is a Python library for learners transitioning from block-based programming to Python.

This guide covers installation, the basic workflow, and the difference between the core library and its optional AI features.

## 1. GitHub Codespaces

The repository includes a development-container configuration for GitHub Codespaces.

### Create a Codespace

1. Open the repository on GitHub.
2. Select **Code → Codespaces**.
3. Create a new Codespace from the `main` branch.
4. Wait for the container to finish building.
5. Open a Python file.

The development container provides Python 3.12 and installs the project and its required dependencies.

### Run a first program

Create `main.py`:

```python
from beyondblocks import ask, say, random_number

name = ask("What is your name?")
print(f"Hello, {name}!")

number = random_number(1, 10)
print("Random number:", number)
```

Run it:

```bash
python main.py
```

### Codespaces audio limitation

`pyttsx3`, used by `say()`, depends on an audio environment. A Codespace is a remote Linux environment and may not have an audio output device. The package can therefore import successfully while `say()` cannot produce audible output.

## 2. Local installation

From the repository root:

```bash
python -m pip install -e .
```

Then:

```python
from beyondblocks import repeat, say

def greet():
    say("Hello!")

repeat(3, greet)
```

Run:

```bash
python main.py
```

## 3. Dependencies

The project's Python dependencies are declared in `pyproject.toml`:

- `pyttsx3` — text-to-speech
- `groq` — AI API access
- `python-dotenv` — local `.env` support

The Codespaces configuration also installs the Linux system dependencies required by the text-to-speech stack.

## 4. Public imports

Use:

```python
from beyondblocks import ask, repeat, forever, wait, say, random_number, explain
```

Do not import internal implementation details such as `handle_error()`.

## 5. AI configuration

Normal library functions do not require an API key.

AI features require:

```text
GROQ_API_KEY
```

For local development, an ignored `.env` file can contain:

```text
GROQ_API_KEY=your_api_key_here
```

A GitHub Codespaces secret can provide the same environment variable without putting the key in the repository.

Never commit a real API key.

## 6. Where to go next

- Function behavior → [API Reference](api-reference.md)
- AI behavior/configuration → [AI Features](ai-features.md)
- Architecture → [Architecture](architecture.md)
- Testing → [Testing](testing.md)
- Runnable programs → `../examples/`
