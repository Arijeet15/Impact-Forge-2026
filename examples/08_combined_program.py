"""A small program combining several Beyond Blocks functions."""

from beyondblocks import ask, random_number, repeat, say, wait

name = ask("What is your name?")

print(f"Hello, {name}!")
say(f"Hello, {name}!")
wait(1)

def give_number():
    number = random_number(1, 10)
    print(f"{name}, your random number is {number}.")
    wait(0.5)

repeat(3, give_number)

print("Done!")
