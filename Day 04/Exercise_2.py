import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
items=int(input("How many items did you order :"))
random.seed(items)

choice=random.randint(0,len(names)-1)

print(f"{names[choice]} is going to pay for the meal")