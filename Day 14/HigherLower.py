import art
from game_data import data
from random import choice
from os import system, name 

def format_data(account):
  '''Format the account data into printable format'''
  account_name=account['name']
  account_descr=account['description']
  account_country=account['country']
  return (f"{account_name}, a {account_descr}, from {account_country}.")

def check_answer(guess, a_followers,b_followers):
  '''Check if the user is correct'''
  if a_followers>b_followers:
    return guess=='a'
  else:
    return guess=='b'

# Display art
print (art.logo)
score=0
game_should_continue=True
# Generate a random account from the game data
account_b=choice(data)

# Make the game repeatable
while game_should_continue:
  
  # Make account at position B become next account at position A
  account_a=account_b
  account_b=choice(data)
  if account_a==account_b:
    account_b=choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}")

  # Ask user for a guess
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct
  # Get follower count of each account
  a_follower_count=account_a['follower_count']
  b_follower_count=account_b['follower_count']

  # Check if the user is correct
  isCorrect=check_answer(guess,a_follower_count,b_follower_count)

  # Clear the screen between rounds
  if name == 'nt':
    system('cls')
  else:
    system('clear')
  print(art.logo)

  # Give user feedback based on their guess
  if isCorrect:
    score+=1
    print(f"You are correct. Your score is {score}")
  else:
    print(f"Sorry! You are wrong. Your score is {score}")
    game_should_continue=False