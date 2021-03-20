# Reading a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing into a file
with open("new_file.txt", mode="w") as file:
    file.write("\nYou are dead too")
