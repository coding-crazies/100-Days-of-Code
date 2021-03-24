from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
# window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

input_box = Entry(width=7)
# input_box.insert(END, string="Enter distance in miles")
input_box.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def convert():
    km_c = round(float(input_box.get()) * 1.609)
    km.config(text=km_c)


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
