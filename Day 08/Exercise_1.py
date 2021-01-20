# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hi")
  print("Hello")
  print("What's up")

greet()

def greet_with_name(name):
  print(f"Hi {name}")
  print(f"Hello {name}")
  print(f"What's up {name}")

greet_with_name("Faran")

def greet_with(name2,location):
  print(f"Hello {name2}")
  print(f"What is it like in {location}?")

greet_with("Faran","Gorakhpur")
greet_with(location="Valorant",name2="Phoenix")