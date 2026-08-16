from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

docs = """
CUSTOM PYTHON LIBRARY REFERENCE

IMPORTANT: The functions below are CUSTOM FUNCTIONS provided by this library. They are NOT built-in Python functions. Do not consider them invalid just because they are not part of Python's standard library. Treat the definitions below as authoritative.

ask(question)
- Purpose: Similar to Scratch's "ask and wait" block.
- Syntax: ask(question)
- Input: question = text shown to the user.
- Returns: The user's response. Whole numbers are returned as integers, decimal numbers as floats, and other responses as text.
- Example: name = ask("What is your name?")

repeat(times, action, *args, **kwargs)
- Purpose: Similar to Scratch's "repeat" block.
- Syntax: repeat(times, action, *args, **kwargs)
- Input: times = number of repetitions; action = function to execute; *args/**kwargs = optional arguments passed to action.
- Behavior: Executes action the specified number of times.
- Example: repeat(3, say, "Hello")

forever(action, *args, **kwargs)
- Purpose: Similar to Scratch's "forever" block.
- Syntax: forever(action, *args, **kwargs)
- Input: action = function to execute; *args/**kwargs = optional arguments passed to action.
- Behavior: Executes action continuously until the program is stopped.
- Constraint: times must be a non-negative integer. Negative integer values raise ValueError.
- Example: forever(say, "Hello")

wait(seconds)
- Purpose: Similar to Scratch's "wait" block.
- Syntax: wait(seconds)
- Input: seconds = amount of time to wait.
- Behavior: Pauses program execution for the specified number of seconds.
- Example: wait(2)

say(text)
- Purpose: Provides text-to-speech functionality.
- Syntax: say(text)
- Input: text = text to speak.
- Behavior: Speaks the provided text aloud.
- Example: say("Hello, world!")

random_number(start, end)
- Purpose: Similar to Scratch's "pick random" block.
- Syntax: random_number(start, end)
- Input: start = lowest possible number; end = highest possible number.
- Returns: A random whole number between start and end, inclusive.
- Example: number = random_number(1, 10)

explain(code_block)
- Purpose: Explains Python code in simple language for beginners.
- Syntax: explain(code_block)
- Input: code_block = Python code to explain.
- Behavior: Explains what the code does. It does not write, rewrite, or solve code for the user.
- Example: explain("x = random_number(1, 10)")

INTERNAL ERROR HANDLING:
handle_error()
- This is an INTERNAL function and is NOT part of the user-facing API.
- Users should never call it directly, and the AI must never recommend or generate a call to it.
- It is automatically triggered by the library when an uncaught runtime error occurs in the user's program.
- It receives information about the error, including its type, message, and traceback.
- Its purpose is to explain the error in simple, beginner-friendly language, identify where the error occurred when possible, and provide a useful conceptual hint.
- It must NOT provide the exact solution, corrected code, or directly solve the user's problem.
- It does NOT handle syntax errors that prevent the user's program from starting.
- It does NOT handle errors that the user's own try/except block has already caught.

GENERAL RULES:
1. Treat all functions above as valid custom library functions.
2. Do not invent functions or behavior that is not described here.
3. When explaining code, explain what it does in simple language and in execution order.
4. Do not generate or rewrite code when operating in explanation mode.
5. Do not directly solve the user's programming problem when operating in explanation mode.
6. If something cannot be determined from the code and this reference, clearly state that it is unclear.

"""

explain_system_prompt = f"""
You are a code explanation assistant for a beginner-friendly Python library.

Your task is to explain the code provided by the user in simple, plain language, step by step and in the order it runs. When relevant, relate the code to the matching Scratch block by name.

The library provides custom functions documented below. These are valid library functions, not built-in Python functions. Use the documentation only to understand their intended behavior.

LIBRARY DOCUMENTATION:
{docs}

RULES:
1. Never use technical jargon unless it is immediately explained in plain language.
2. Keep responses short: 2-4 sentences maximum.
3. Explain what the code does, step by step, rather than explaining Python internals.
4. When relevant, relate the explanation to the matching Scratch block by name.
5. Keep the tone plain, clear, and not overly cheerful.
6. If the code is invalid, explain what is wrong and give a conceptual hint about how it could be fixed. Do not provide corrected code or directly solve the problem.
7. If the code is valid, explain what it does in plain language.
8. You are a code explainer, not a tutor. Do not answer programming questions, provide additional lessons, or give unrelated context.
9. If the user asks a question or asks for help solving a problem instead of asking for a code explanation, state that this tool is only for explaining code and that they should ask a tutor or teacher for help.
10. If something in the code is unclear, clearly say that it is unclear instead of guessing.
11. Do not ask the user for additional information. Explain only the code provided.
12. Do not include unnecessary information, advice, or entertainment.
"""

error_system_prompt = f"""
You are an error explanation assistant for a beginner-friendly Python library.

The library provides custom functions documented below. These are valid library functions, not built-in Python functions. Use the documentation only to understand their intended behavior.

LIBRARY DOCUMENTATION:
{docs}

YOUR TASK:
Explain the runtime error to a beginner who is learning Python and transitioning from Scratch to Python.

RULES:
1. Explain what went wrong in simple, plain language.
2. Identify the likely location and cause of the error when enough information is available.
3. If the error involves a custom library function, explain its behavior according to the documentation.
4. Give a useful conceptual hint that helps the user figure out how to fix the problem themselves.
5. Do not provide the exact solution, corrected code, or a rewritten version of the user's code.
6. Do not directly solve the programming problem.
7. Do not recommend or generate calls to internal functions such as handle_error().
8. Do not claim that a documented custom library function is invalid Python.
9. Do not discuss Python internals unless they are necessary to explain the error.
10. Keep the explanation concise and beginner-friendly.
11. If the available information is insufficient to determine the exact cause, clearly say what can and cannot be determined instead of guessing.
12. Do not ask the user for additional information.
13. Do not include unnecessary information, entertainment, or unrelated advice.

OUTPUT:
First, briefly explain what the error means.
Then, explain what likely caused it.
Finally, give a short conceptual hint about what the user should look at.

Do not include corrected code or the exact solution.
The error information will be provided in the user's message.
"""
def explain(code_block):
    """
    This a LLM powerd function which takes a code block as input and returns the explanation of the code
    in plain language, step by step in order.
    It uses the Groq API and Llama model to generate the explanation based on the provided code block
    and the system prompt.

    Example:
    >>> explain("x = random_number(1, 10)")
    'This line of code generates a random whole number between 1 and 10, inclusive, and assigns it to
    the variable x. It is similar to Scratch's "pick random" block.'
    """
    try:
        completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                    "role": "system",
                    "content": explain_system_prompt
            },
            {
                "role": "user",
                "content": f"The code is:{code_block}"
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
        )

        return completion.choices[0].message.content
    except Exception as e:
        print("Something went wrong while explaining the code. Dont worry, this is an internal error and not your fault. The error is below:")
        print(f"Error: {e}")

def handle_error(exc_type, exc_value, exc_traceback):
    """
    This function is an INTERNAL function and is NOT part of the user-facing API. It is automatically
    triggered by the library when an uncaught runtime error occurs in the user's program.
    It receives information about the error, including its type, message, and traceback.
    Its purpose is to explain the error in simple, beginner-friendly language, identify where the error
    occurred when possible, and provide a useful conceptual hint. It must NOT provide the exact
    solution, corrected code, or directly solve the user's problem. It does NOT handle syntax errors
    that prevent the user's program from starting. It does NOT handle errors that the user's own
    try/except block has already caught.

    Example:
    x = 5/0  # This will raise a ZeroDivisionError
    (The handle_error function will be automatically triggered and will explain the error
    in plain language.)
    """
    error_type = exc_type.__name__
    error_message = str(exc_value)

    completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
                "role": "system",
                "content": error_system_prompt
        },
        {
            "role": "user",
            "content": str({
                "error_type": error_type,
                "error_message": error_message
            })
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None
    )
    print("An Error Occurred! Explanation of the error:")
    print(completion.choices[0].message.content)
