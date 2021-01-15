#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

lucky=int(input("Enter your lucky number: "))
random.seed(lucky)

random_number=random.randint(0,1)

if random_number == 0:
  print("Heads")
else:
  print("Tails")