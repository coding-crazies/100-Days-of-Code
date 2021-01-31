from art import logo
import random

def check_answer(guess,answer):
    if guess==answer:
        return True
    return False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
answer=random.randint(1,100)
print(f"Psst! The number is {answer}")
level=input("Choose a difficulty 'easy' or 'hard': ")
# if level=='easy':
#     steps=10
# elif level=='hard':
#     steps=5
# else:
#     print("Wrong input!")
guess=int(input("Make a guess: "))
