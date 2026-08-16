# Library Functions

This document describes the public Beyond Blocks API/Functions of the Beyond Blocks Library.

| Function | Purpose |
|---|---|
| `ask()` | Beginner-friendly input with common numeric conversion |
| `repeat()` | Repeats a callable |
| `forever()` | Repeatedly executes a callable |
| `wait()` | Pauses execution |
| `say()` | Text-to-speech |
| `random_number()` | Inclusive random integer |
| `explain()` | AI-powered code explanation |

---

## `ask()`

### Syntax

```python
ask(question)
```

### Behavior

The user's response is converted when possible:

- whole-number text → `int`
- decimal-number text → `float`
- other input → `str`

### Example

```python
from beyondblocks import ask

name = ask("What is your name?")
age = ask("How old are you?")
print(name, age)
```

### Why it exists

Python's `input()` always returns text. `ask()` handles common numeric conversion automatically to reduce early friction for beginners.

---

## `repeat()`

### Syntax

```python
repeat(times, action, *args, **kwargs)
```

### Behavior

Executes `action` exactly `times` times and passes the supplied arguments to it.

A negative integer value for `times` raises `ValueError`.

### Examples

```python
from beyondblocks import repeat

def greet():
    print("Hello!")

repeat(3, greet)
```

```python
repeat(3, print, "Hello!")
```

### Why it exists

It gives a learner coming from a block-based `repeat` operation a familiar entry point while still using real Python callables and arguments.

---

## `forever()`

### Syntax

```python
forever(action, *args, **kwargs)
```

### Behavior

Repeatedly executes `action` until the program is stopped.

### Example

```python
from beyondblocks import forever

def main():
    print("Program is running")

forever(main)
```

### Why it exists

It provides a familiar equivalent to a block-based `forever` concept.

---

## `wait()`

### Syntax

```python
wait(seconds)
```

### Behavior

Pauses execution for the specified number of seconds.

### Example

```python
from beyondblocks import wait

print("Start")
wait(2)
print("Two seconds later")
```

### Implementation

Uses Python's standard `time.sleep()` functionality.

---

## `say()`

### Syntax

```python
say(text)
```

### Behavior

Uses text-to-speech to speak the supplied text.

### Example

```python
from beyondblocks import say

say("Hello, world!")
```

### Important distinction

`say()` is not a replacement for `print()`.

- `print()` writes text to the terminal.
- `say()` attempts to speak the text through the system audio environment.

### Implementation

Uses `pyttsx3`.

### Environment limitation

A remote Codespace may not have a usable audio output device, so `say()` may not produce audible output there.

---

## `random_number()`

### Syntax

```python
random_number(start, end)
```

### Behavior

Returns a random `int` between `start` and `end`, inclusive.

### Example

```python
from beyondblocks import random_number

number = random_number(1, 10)
print(number)
```

### Why it exists

It provides a familiar block-based “pick random” concept using a normal Python return value.

---

## `explain()`

### Syntax

```python
explain(code_block)
```

### Behavior

Uses the Groq API to return a beginner-friendly explanation of the supplied Python code.

### Example

```python
from beyondblocks import explain

result = explain("x = random_number(1, 10)")
print(result)
```

### Intended behavior

The AI system is instructed to:

- use plain language
- explain execution order
- recognize documented Beyond Blocks functions
- connect relevant functions to block-based concepts
- explain recognizable errors
- avoid rewriting the user's code
- avoid directly solving unrelated programming questions

### Requirement

Requires `GROQ_API_KEY` and network access to Groq.

---

## Internal `handle_error()`

`handle_error()` is intentionally not part of the public API.

It is called automatically through the library's exception-hook mechanism when an uncaught runtime error occurs.

Users should not import or call it directly.

Its purpose is to obtain a beginner-friendly AI explanation of the uncaught runtime error.

---

## Function selection

```text
Need input?               -> ask()
Need repetition?          -> repeat()
Need continuous loop?     -> forever()
Need a delay?             -> wait()
Need speech?              -> say()
Need a random integer?    -> random_number()
Need an AI explanation?   -> explain()
```
