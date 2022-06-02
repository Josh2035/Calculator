#Josh Hayes
#Calculator
from tkinter import *
import tkinter as tk

def add():
    e1.insert("2")


root=tk.Tk()
root.geometry("207x355")
root.title("calc")
buttons=['*','7','8','9','+','4','5','6','-','1','2','3','/','.','=']
rows=['0','1','1','1','1','2','2','2','2','3','3','3','3','4','4',]
columns=['3','0','1','2','3','0','1','2','3','0','1','2','3','2','3',]
buttons2=['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12','b13','b15','b16']

for x,y,z,t in zip(buttons,rows,columns,buttons2):
    t=tk.Button(root, text=x, width=6, height=4, bg="black", fg="lime", activebackground="lime", command=add)
    t.grid(row=y,column=z,)


#0 Button
b14=tk.Button(root,text=0,width=13, height=4, bg="black", fg="lime", activebackground="lime", command=cool)
b14.grid(row=4,column=0,columnspan=2)
e1=tk.Entry(root,bg="black", fg="lime", width=25)
e1.grid(row=0,column=0,columnspan=3)
root.mainloop()
