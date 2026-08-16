"""Using wait() and random_number()."""

from beyondblocks import random_number, wait

print("Generating a random number...")
wait(2)

number = random_number(1, 10)
print(f"Your random number is: {number}")
