# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nameU=name1+name2
name=nameU.lower()
s1=0
s2=0

s1=name.count('t')+name.count('r')+name.count('u')+name.count('e')
s2=name.count('l')+name.count('o')+name.count('v')+name.count('e')

ss=str(s1)+str(s2)
s=int(ss)
if (s<10 or s>90):
  print(f"Your score is {s}, you go together like coke and mentos.")
elif (s>=40 and s<=50):
  print(f"Your score is {s}, you are alright together.")
else:
  print(f"Your score is {s}")