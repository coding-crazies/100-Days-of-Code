def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

from art import logo
print(logo)

flag='n'
while flag=='n':
  num1=int(input("What's the first number? "))
  print("+")
  print("-")
  print("*")
  print("/")
  flag='y'
  while flag=='y':
    sym=input("Pick an operation: ")
    num2=int(input("What's the next number? "))

    if sym=="+":
      sol=add(num1,num2)
      print(f"{num1} {sym} {num2} = {sol}")
    elif sym=="-":
      sol=subtract(num1,num2)
      print(f"{num1} {sym} {num2} = {sol}")
    elif sym=="*":
      sol=multiply(num1,num2)
      print(f"{num1} {sym} {num2} = {sol}")
    elif sym=="/":
      sol=divide(num1,num2)
      print(f"{num1} {sym} {num2} = {sol}")
    else:
      print("Invalid input")
    num1=sol

    flag=input(f"Type 'y' to continue calculating with {sol}, or type 'n' to start a new calculation: ")