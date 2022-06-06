import tkinter as tk
import time
# Defining Buttons (Maybe could do this in a loop to make it easier, but it seems the lambda:add() command doesn't work
# with Tkinter buttons or at least with the list comprehension I'm using


def b1(): en1.insert("end", '*')
def b2(): en1.insert("end", '7')
def b3(): en1.insert("end", '8')
def b4(): en1.insert("end", '9')
def b5(): en1.insert("end", '+')
def b6(): en1.insert("end", '4')
def b7(): en1.insert("end", '5')
def b8(): en1.insert("end", '6')
def b9(): en1.insert("end", '-')
def b10(): en1.insert("end", '1')
def b11(): en1.insert("end", '2')
def b12(): en1.insert("end", '3')
def b13(): en1.insert("end", '/')
def b14(): en1.insert("end", '0')
def b15(): en1.insert("end", '.')


def equal():
    try:
        answer = en1.get()
        en1.delete(0, 'end')
        en1.insert("end", eval(answer))
    except:
        en1.delete(0, 'end')
        en1.insert('end', 'ERROR')
        en1.delete(0, 'end')


root = tk.Tk()
root.geometry("207x355")
root.title("calc")

# en1 is the Entry
en1 = tk.Entry(root, width=25)
en1.grid(row=0, column=0, columnspan=3)

#
eq1 = tk.Button(root, text='=', width=6, height=4, command=equal)
eq1.grid(row='4', column='3')

buttons = ['*', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '/', '.']
rows = ['0', '1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4']
columns = ['3', '0', '1', '2', '3', '0', '1', '2', '3', '0', '1', '2', '3', '2']
buttons2 = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b15']
functions = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b15]

for x, y, z, t, f in zip(buttons, rows, columns, buttons2, functions):
    t = tk.Button(root, text=x, width=6, height=4, command=f)
    t.grid(row=y, column=z)

# 0 Button has a different size could just do an if statement, but it'd look the same
b14 = tk.Button(root, text=0, width=13, height=4, command=b14)
b14.grid(row=4, column=0, columnspan=2)

root.mainloop()
