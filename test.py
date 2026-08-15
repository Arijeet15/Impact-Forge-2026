# Actual Python:
import time

print("Hello, World!")
time.sleep(1)    
name = input("What is your name? ")
age = int(input("What is your age? "))
time.sleep(1)
print(f"You are {name} and next year you will be {age+1} years old.")

# My code:
from main import *

print("Hello, World!")
wait(1)
name = ask("What is your name?")
age = ask("What is your age?")
wait(1)
print(f"You are {name} and next year you will be {age+1} years old.")


