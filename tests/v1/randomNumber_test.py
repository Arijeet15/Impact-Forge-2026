from main import random_number, repeat

def print_random_number():
    number = random_number(1, 100)
    print(f"Random number: {number}")

repeat(5, print_random_number)

# TEST SUCESSFULL
