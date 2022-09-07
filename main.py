import random
from logo import logo

EASY = 10
HARD = 5


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY
    elif level == "hard":
        return HARD


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High ⬆️")
        return turns - 1

    elif guess < answer:
        print("Too Low ⬇️")
        return turns - 1

    elif guess == answer:
        print("correct Guess 😊")


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    print(f"Pssst, the correct answer is {answer}")

    turns = difficulty()

    guess = 0

    while guess != answer:

        print(f"you have {turns} attempts remaining to guess a number")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("Game over, you run out of Guess")
            break
        elif guess != answer:
            print("guess again")




game()
