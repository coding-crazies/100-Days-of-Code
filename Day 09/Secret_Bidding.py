from replit import clear
#HINT: You can call clear() to clear the output in the console.

def bid_calculate():
  greatest=0
  winner=""
  for key in bidders:
    if bidders[key]>greatest:
      greatest=bidders[key]
      winner=key
  print(f"The winner is {winner} with a bid of {greatest}")
bidders={}
flag='yes'
from art import logo
print(logo)
while flag=='yes':
  name=input("What is your name? ")
  bid=int(input("What is your bid? ₹"))
  bidders[name]=bid
  flag=input("Are there any other bidders? Type 'yes ' or 'no' ")
  if flag=='yes':
    clear()
  else:
    bid_calculate()