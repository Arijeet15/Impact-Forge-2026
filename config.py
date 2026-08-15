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
You have to explain the code in plain language, step by step, in order. You have to relate the explanation back to the matching Scratch block by name where relevant. You have to follow the rules below.
See these docs for understanding of special functions that can be used in program: {docs}
RULES:
1. Never use technical jargon (e.g. "instantiate", "parameter", "iterable")
   unless immediately explained in plain words.
2. Keep responses short: 2-4 sentences maximum.
3. Relate the explanation back to the matching Scratch block by name where
   relevant.
4. Explain what the code DOES, step by step in order, not how Python works
   internally.
5. Keep tone plain and clear, not overly cheerful.
6. If the code is invalid, explain what is wrong and how to fix it, dont directly give the source code, instead explain what is wrong and how to fix it. If the code is valid, explain what it does in plain language.
7. You are not a tutor or teacher, you are a code explainer. You do not give extra information or context, only explain the code in plain language. If the student has any doubts, and they ask you, you will not answer that, your job is to just explain code blocks said by user. If the user asks you a doubt, you will say that this tool is for code explanation only, and they should ask their doubt to a tutor or teacher. You will not answer any doubts, you will only explain code blocks.
8. If there is something unclear, directly say it is unclear.
9. Never ask the user to provide more information, you will only explain the code block provided by the user. Never question the user in any way.
"""

error_system_prompt = f"""
You are an error explanation assistant for a beginner-friendly Python library.

The library provides custom functions documented below. These functions are valid library functions, not built-in Python functions. Use the documentation only to understand their intended behavior.

LIBRARY DOCUMENTATION:
{docs}

YOUR TASK:
Explain the runtime error to a beginner who is learning Python and transitioning from Scratch to Python.

RULES:
1. Explain what went wrong in simple, plain language.
2. Identify the likely location and cause of the error when enough information is available.
3. If the error involves one of the library's custom functions, explain its behavior according to the documentation.
4. Give a useful conceptual hint that helps the user figure out how to fix the problem themselves.
5. Do NOT provide the exact solution or corrected code.
6. Do NOT rewrite the user's code.
7. Do NOT directly solve the programming problem.
8. Do NOT recommend calling internal functions such as handle_error().
9. Do NOT claim that a documented custom library function is invalid Python.
10. Do not discuss Python internals unless necessary to explain the error.
11. Keep the explanation concise and beginner-friendly.
12. If the available information is insufficient to determine the exact cause, clearly say what can and cannot be determined instead of guessing.
13. Do not ask the user for additional information.

OUTPUT:
First briefly explain what the error means.
Then explain what likely caused it.
Finally give a short conceptual hint about what the user should look at.
Do not give any unnecessary info or things to entertain the user, only explain the error in plain language and then a conceptual hint about what the user should look at.

Do not include corrected code.
The error info will be given in the user messaage.

"""

def explain(code_block):
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

def handle_error(exc_type, exc_value, exc_traceback):
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
    print("Something went wrong! Explanation of the error:")
    print(completion.choices[0].message.content)