import tkinter
from tkinter import *


window = Tk()
window.title("first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#label
my_label = tkinter.Label(text="ULTRA LABEL", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)



#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()


