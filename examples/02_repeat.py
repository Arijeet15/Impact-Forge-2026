"""Using repeat() with a normal Python function."""

from beyondblocks import repeat

def greet(name):
    print(f"Hello, {name}!")

repeat(3, greet, "Arijeet")
