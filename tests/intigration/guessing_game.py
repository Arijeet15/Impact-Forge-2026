from beyondblocks.core import ask, repeat, wait, say, random_number, explain


# A small guessing game that combines:
# ask(), repeat(), wait(), say(), random_number(), and explain()

secret_number = random_number(1, 20)
attempts = 0
won = False


def make_guess():
    global attempts, won

    attempts += 1
    guess = ask(f"Attempt {attempts}/5 - Guess a number between 1 and 20: ")

    if guess == secret_number:
        say("Correct! You guessed the number!")
        won = True
    elif guess < secret_number:
        say("Too low!")
    else:
        say("Too high!")

    if not won:
        wait(0.5)


say("Welcome to the number guessing game!")
say("I have chosen a number between 1 and 20.")

repeat(5, make_guess)

if won:
    say(f"You won in {attempts} attempts!")
else:
    say(f"Game over! The number was {secret_number}.")

explain("""
secret_number = random_number(1, 20)
repeat(5, make_guess)
""")