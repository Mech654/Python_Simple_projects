from tkinter import *

root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))


    if math == "subtraction":
        e.insert(0, f_num - int(second_number))


    if math == "divide":
        e.insert(0, f_num / int(second_number))


    if math == "multiply":
        e.insert(0, f_num * int(second_number))




Button0 = Button(root, text='0', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(0)).grid(row=4, column=0)
Button1 = Button(root, text='1', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(1)).grid(row=3, column=0)
Button2 = Button(root, text='2', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(2)).grid(row=3, column=1)
Button3 = Button(root, text='3', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(3)).grid(row=3, column=2)
Button4 = Button(root, text='4', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(4)).grid(row=2, column=0)
Button5 = Button(root, text='5', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(5)).grid(row=2, column=1)
Button6 = Button(root, text='6', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(6)).grid(row=2, column=2)
Button7 = Button(root, text='7', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(7)).grid(row=1, column=0)
Button8 = Button(root, text='8', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(8)).grid(row=1, column=1)
Button9 = Button(root, text='9', padx=50, pady=50, fg='black', bg='orange', command=lambda: button_click(9)).grid(row=1, column=2)

Button_clear = Button(root, text='clear', padx=40, pady=50, fg='black', bg='red', command=button_clear).grid(row=4, column=1)
Button_calculate = Button(root, text='=', padx=50, pady=50, fg='black', bg='green', command=button_equal).grid(row=4, column=2)


operator_1 = Button(root, text='+', padx=51, pady=50, fg='black', bg='gray', command=button_add).grid(row=1, column=3)
operator_2 = Button(root, text='-', padx=53, pady=50, fg='black', bg='gray', comman=button_subtraction).grid(row=2, column=3)
operator_3 = Button(root, text='*', padx=53, pady=50, fg='black', bg='gray', command=button_multiply).grid(row=3, column=3)
operator_4 = Button(root, text='/', padx=53, pady=50, fg='black', bg='gray', command=button_divide).grid(row=4, column=3)


root.mainloop()