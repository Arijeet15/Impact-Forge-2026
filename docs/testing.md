# Testing

Beyond Blocks was tested in multiple stages.

## V1 — Function-level testing

V1 focused on expected behavior of individual functions.

The suite covered the main functions, including:

- `ask()`
- `repeat()`
- `forever()`
- `wait()`
- `say()`
- `random_number()`
- `explain()`
- error handling

The purpose was to verify the functions independently.

---

## V2 — Edge-case testing

V2 deliberately tested behavior outside the simplest successful path.

The testing approach included:

- unusual values
- different parameters
- different actions
- invalid input
- boundary cases
- combinations of optional arguments
- attempts to break implementation assumptions

The goal was effectively to test what happens when a beginner supplies unexpected inputs instead of only ideal inputs.

Changes found during V2 were implemented and the updated tests were rerun.

---

## Public API testing

The package was tested through its intended public interface:

```python
from beyondblocks import (
    ask,
    repeat,
    forever,
    wait,
    say,
    random_number,
    explain,
)
```

Testing also confirmed that internal `handle_error()` is not exposed through the public API.

---

## Package installation testing

The project was installed with:

```bash
python -m pip install -e .
```

The package was then imported from outside the package directory.

This verifies the actual installed package interface rather than relying on local file proximity.

---

## Cross-environment testing

The project was tested in:

- the primary development environment
- a downloaded ZIP copy
- a fresh GitHub Codespace

This revealed environment-specific issues that unit tests alone cannot detect.

For example, the Codespace environment required Linux text-to-speech dependencies and still did not provide an audio output device for `say()`.

---

## AI testing

With `GROQ_API_KEY` configured, the following kind of call was tested successfully in the Codespace:

```python
from beyondblocks import explain

print(explain("x = random_number(1, 10)"))
```

The result was a beginner-friendly explanation.

The missing-key behavior was also tested to ensure that importing the package does not require AI credentials.

---

## Integration testing

Integration testing is intentionally lightweight in this version.

The main effort was placed on:

1. individual function behavior
2. edge cases
3. public API/package imports
4. cross-environment validation
5. AI integration

A larger end-to-end integration suite can be added in a future version.
