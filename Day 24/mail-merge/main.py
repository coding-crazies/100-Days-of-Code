# TODO: Create a letter using starting_letter.txt
names = open("./Input/Names/invited_names.txt", "r")
name_list = names.readlines()
names.close()
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for name in name_list:
    stripped_name = name.strip()
    with open(f"./Input/Letters/starting_letter.txt",
              mode="r") as file:
        contents = file.read()
        new = contents.replace("[name]", f"{stripped_name}")
        output = open(f"./Output/ReadyToSend/invite_for_{name}.docx", "w")
        output.write(new)
        output.close()
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
