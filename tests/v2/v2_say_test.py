from beyondblocks.core import say

say_values = [
    "Hello, World!",
    "Hello",
    "",
    "Hello, how are you?",
    "123456789",
    "Hello! @#$%^&*()",
    "ppppppp",
    "This is a longer sentence to test text to speech.",
    123,
    3.14,
    True,
    False,
    None,
    "नमस्ते",
    "こんにちは",
    "你好",
    "😂😭💔",
    "A short sentence with many different words and punctuation!"
]

for value in say_values:
    print(f"Testing say({value})")
    try:
        say(value)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Hello, World!")
# engine.runAndWait()
# print("Successfully said 'Hello, World!' using text-to-speech.")

# engine.say("Hello")
# engine.runAndWait()
# print("Successfully said 'Hello' using text-to-speech.")

"""
Important Testing Outcome:
The say() function relies on pyttsx3 and therefore depends heavily on the speech engine, voice, and TTS backend available on the user's system. Consistent behavior cannot be guaranteed across environments.

During testing, pyttsx3 did not raise an exception when subsequent speech output failed. Instead, say() returned normally, causing the calling program to interpret the operation as successful even though no speech was produced.

Conclusion: The current implementation of say() cannot reliably determine whether speech was actually produced. This is an environment/backend limitation that should be documented.
"""

# TEST DONE - CAN NOT BE RELIABILY CLASSIFFIED AS SUCESS OR FAILURE
