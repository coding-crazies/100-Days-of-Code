import tkinter

window = tkinter.Tk()

window.title("Random GUI shit")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Faran Mohammad", font=("Helvetica", 24, "italic"))
my_label.pack()

window.mainloop()
