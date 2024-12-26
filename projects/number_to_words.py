from num2words import num2words
from tkinter import *

def num_to_words():
    given_num = float(num.get())
    num_in_word = num2words(given_num)
    display.config(text=str(num_in_word).capitalize())

root = Tk()
root.title("Number to Words")
root.geometry("650x400")

num = StringVar()

# Adding title
title = Label(root, text="Number to words converter", fg="blue", font=("Arial", 20, "bold"))
title.place(x=220, y=10)

# Options
format_lable = Label(root, text="Format supported: ", fg="black", font=("Arial", 10, "bold"))
format_lable.place(x=100, y=70)

pos_format_lable = Label(root, text="Positive numbers", fg="black", font=("Arial", 10, "bold"))
pos_format_lable.place(x=200, y=90)

neg_format_lable = Label(root, text="Negative numbers", fg="black", font=("Arial", 10, "bold"))
neg_format_lable.place(x=200, y=110)

float_format_lable = Label(root, text="Floating point numbers", fg="black", font=("Arial", 10, "bold"))
float_format_lable.place(x=200, y=130)

zero_format_lable = Label(root, text="Zero", fg="black", font=("Arial", 10, "bold"))
zero_format_lable.place(x=200, y=150)

num_entry_lable = Label(root, text="Enter number: ", fg="black", font=("Arial", 15, "bold"))
num_entry_lable.place(x=50, y=200)

num_entry = Entry(root, textvariable=num, width=30)
num_entry.place(x=200, y=200)

btn = Button(master=root, text="Calculate", fg="black", font=("Arial", 15, "bold"), command=num_to_words)
btn.place(x=280, y=230)

display = Label(root, text="", fg="black", font=("Arial", 15, "bold"))
display.place(x=10, y=300)

# Use the provided absolute path for the file
photo = PhotoImage(file="E:\\2022 PYTHON UDEMY 2022\\practice\\number.png")
root.iconphoto(False, photo)

root.mainloop()
