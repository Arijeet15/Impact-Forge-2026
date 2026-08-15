from main import repeat

def greet(name):
    print(f"Hello, {name}!")

repeat(5, greet, "Arijeet")

def compliment(name, name2):
    print(f"{name}, {name2}, you are awesome!")

repeat(3, compliment, "Arijeet", "John")

# TEST SUCESSFULL
