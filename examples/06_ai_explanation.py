"""Using the AI code explanation feature.

Requires GROQ_API_KEY to be configured in the environment.
"""

from beyondblocks import explain

code = """
number = random_number(1, 10)
print(number)
"""

print(explain(code))
