"""Demonstrate automatic AI explanation of an uncaught runtime error.

Requires GROQ_API_KEY to be configured.

This example is intentionally supposed to fail so the library's
automatic runtime-error explanation can run.
"""

from beyondblocks import wait       # 'wait' is imported to give the user time to read the output before the program crashes

print("The next line will intentionally cause a runtime error.")
wait(2)  # wait 2 seconds before the error occurs

number = 10
result = number / 0

print(result)
