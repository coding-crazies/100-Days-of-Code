from tkinter import *

window = Tk()

window.title("Random GUI shit")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Faran Mohammad", font=("Helvetica", 24, "italic"))
my_label.grid(column=0, row=0)


def clicked():
    my_label["text"] = input.get()


# Button
my_button = Button(text="Click Me!", command=clicked)
my_button.grid(column=1, row=1)

# Entry
input = Entry()
input.grid(column=3, row=2)

# New Button
new_button = Button(text="New Click")
new_button.grid(column=2, row=0)

window.mainloop()
