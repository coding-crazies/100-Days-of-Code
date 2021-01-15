import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choiceList=[rock,paper,scissors]

userInput=int(input("What do you choose? Press 0 for rock, 1 for paper and 2 for scissors : "))

userChoice=choiceList[userInput]
randomGenerator=random.randint(0,2)

systemChoice=choiceList[randomGenerator]

if userChoice==choiceList[0]:
  print(userChoice)
  print("Computer chose:")
  print(systemChoice)
  if systemChoice==choiceList[1]:
    print("You lose")
  elif systemChoice==choiceList[2]:
    print("You won")
  else:
    print("It's a draw")
elif userChoice==choiceList[1]:
  print(userChoice)
  print(systemChoice)
  print("Computer chose:")
  if systemChoice==choiceList[2]:
    print("You lose")
  elif systemChoice==choiceList[0]:
    print("You won")
  else:
    print("It's a draw")
elif userChoice==choiceList[2]:
  print(userChoice)
  print(systemChoice)
  print("Computer chose:")
  if systemChoice==choiceList[0]:
    print("You lose")
  elif systemChoice==choiceList[1]:
    print("You won")
  else:
    print("It's a draw")