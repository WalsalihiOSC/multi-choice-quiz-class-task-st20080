global total

y=0  
from tkinter import *
from tkinter import ttk
n= ttk.Notebook()
f1= ttk.Frame(n)

window= ttk.Frame(n)


def main(x):
    global total
    n.add(f1, text="Question")

    total= ttk.Label(window, text="0")


    Label(f1, text="What is the population of NZ").grid(row=2,column=2)
    Button(f1, text="5 Million", command=correct).grid(row=3,column=1)
    Button(f1, text="10 Million", command=incorrect).grid(row=3,column=2)
    Button(f1, text="30 Million", command=incorrect).grid(row=3,column=3)

def correct():
    global total
    Label(f1, text="Correct").grid(row=1,column=2)

def incorrect():
    Label(f1, text="Incorrect").grid(row=1,column=2)

main(y)


n.pack()

n.mainloop()
