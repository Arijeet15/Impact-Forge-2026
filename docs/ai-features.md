# AI Features

Beyond Blocks uses the GroqCloud API for two related features:

1. `explain()` — explains Python code.
2. Automatic runtime-error explanation — explains uncaught runtime errors.

The AI layer is intended to help a learner understand Python rather than generate the learner's solution.

---

## `explain()`

Example:

```python
from beyondblocks import explain

print(explain("""
number = random_number(1, 10)
print(number)
"""))
```

The model is instructed to:

- use simple language
- explain code in execution order
- recognize Beyond Blocks functions as documented custom functions
- relate relevant functions to block-based concepts
- explain recognizable errors
- avoid corrected code
- avoid directly solving unrelated programming questions

It is an explanation feature, not a general code-generation feature.

---

## Automatic runtime-error explanation

Beyond Blocks installs a custom `sys.excepthook`.

The high-level flow is:

```text
Uncaught runtime error
        |
        v
Beyond Blocks exception hook
        |
        v
handle_error(...)
        |
        v
Groq API
        |
        v
Beginner-friendly explanation
```

The AI receives the error type/message information and is instructed to explain:

1. what happened
2. the likely cause/location when available
3. the relevant concept
4. a conceptual hint

It is not instructed to provide the exact corrected code.

### Important boundaries

This mechanism does not handle every possible failure:

- syntax errors that prevent program startup do not reach the runtime exception hook
- errors caught by the user's own `try/except` do not reach the global exception hook
- network/API failures can prevent an AI explanation

---

# API key

AI features require:

```text
GROQ_API_KEY
```

## Local `.env`

Example:

```text
GROQ_API_KEY=your_api_key_here
```

Keep `.env` ignored by Git.

## GitHub Codespaces

A Codespaces secret can provide `GROQ_API_KEY` to the environment without storing the credential in the repository.

Never commit or publish a real API key.

---

# Optional AI layer

The package can be imported without an API key.

Normal functions such as:

```python
from beyondblocks import ask, repeat, random_number
```

do not require Groq.

The AI client is needed only when an AI feature is actually used.

This keeps the optional AI layer separate from the core library.

---

# External service considerations

The AI layer depends on:

- network access
- a valid Groq API key
- availability of the external service
- the model's generated output

AI-generated explanations can occasionally be incomplete or incorrect.

The AI layer should therefore be treated as an optional service component rather than a requirement for the basic functions.

---

# Security

Never put a real API key in:

- source code
- README/documentation
- examples
- screenshots
- Git commits

Use environment variables or secure environment secrets.

If an API key is exposed, rotate/revoke it through the provider.
