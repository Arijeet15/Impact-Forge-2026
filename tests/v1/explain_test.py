from beyondblocks.core import explain

code = """
def tellNameAndAge(name, age):
    print(f"You are {name} and you are {age} years old.")

name = ask("What is your name?")
wait(1)
age = ask("What is your age?")
wait(1)
repeat(3, tellNameAndAge, name, age)
"""

explaination = explain(code)
print(explaination)

# TEST SUCESSFULL
