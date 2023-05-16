import tkinter as tk
first_number = 0.0
second_number = 0.0
calculation = ""
equal = True
no_number = True

screen = tk.Tk()

display = tk.Entry(width=18, font=("times new roman", 40), state="disabled",
                   disabledbackground="white", disabledforeground="black")
display.pack(pady=5, padx=5)


def number_click(x):
    global equal
    global no_number
    if equal:
        display["state"] = "normal"
        display.insert(tk.END, x)
        display["state"] = "disabled"
    else:
        display["state"] = "normal"
        display.delete(0, tk.END)
        display.insert(tk.END, x)
        display["state"] = "disabled"
        equal = True
    no_number = False


def dot_click(x):
    if "." in display.get():
        pass
    else:
        global equal
        if equal:
            display["state"] = "normal"
            display.insert(tk.END, x)
            display["state"] = "disabled"
        else:
            display["state"] = "normal"
            display.delete(0, tk.END)
            display.insert(tk.END, x)
            display["state"] = "disabled"
            equal = True


def plus_click():
    if no_number:
        pass
    else:
        global first_number
        global calculation
        if calculation == "+":
            pass
        elif calculation == "":
            first_number = display.get()
            display["state"] = "normal"
            display.delete(0, tk.END)
            display["state"] = "disabled"
            calculation = "+"
        else:
            calculation = "+"


def minus_click():
    if no_number:
        pass
    else:
        global first_number
        global calculation
        if calculation == "-":
            pass
        elif calculation == "":
            first_number = display.get()
            display["state"] = "normal"
            display.delete(0, tk.END)
            display["state"] = "disabled"
            calculation = "-"
        else:
            calculation = "-"


def multiply_click():
    if no_number:
        pass
    else:
        global first_number
        global calculation
        if calculation == "*":
            pass
        elif calculation == "":
            first_number = display.get()
            display["state"] = "normal"
            display.delete(0, tk.END)
            display["state"] = "disabled"
            calculation = "*"
        else:
            calculation = "*"


def divide_click():
    if no_number:
        pass
    else:
        global first_number
        global calculation
        if calculation == "/":
            pass
        elif calculation == "":
            first_number = display.get()
            display["state"] = "normal"
            display.delete(0, tk.END)
            display["state"] = "disabled"
            calculation = "/"
        else:
            calculation = "/"


def equal_click():
    global equal
    if not equal:
        pass
    else:
        try:
            global second_number
            global calculation
            equal = False
            math = ""
            second_number = display.get()
            display["state"] = "normal"
            display.delete(0, tk.END)
            if calculation == "+":
                math = float(first_number) + float(second_number)
            elif calculation == "-":
                math = float(first_number) - float(second_number)
            elif calculation == "*":
                math = float(first_number) * float(second_number)
            elif calculation == "/":
                math = float(first_number) / float(second_number)
            display.insert(0, math)
            display["state"] = "disabled"
            calculation = ""
        except ValueError:
            pass


def clear_all():
    global first_number, second_number, display, calculation
    global equal, no_number
    first_number = 0.0
    second_number = 0.0
    calculation = ""
    display["state"] = "normal"
    display.delete(0, tk.END)
    display["state"] = "disabled"
    equal = True
    no_number = True


Button_Frame = tk.Frame(screen)
Button_Frame.pack(padx=10,pady=10)

Button_7 = tk.Button(Button_Frame, text=7, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=7: number_click(a))
Button_7.grid(row=1, column=0, padx=3, pady=3)

Button_8 = tk.Button(Button_Frame, text=8, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=8: number_click(a))
Button_8.grid(row=1, column=1, padx=3, pady=3)

Button_9 = tk.Button(Button_Frame, text=9, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=9: number_click(a))
Button_9.grid(row=1, column=2, padx=3, pady=3)

Button_4 = tk.Button(Button_Frame, text=4, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=4: number_click(a))
Button_4.grid(row=2, column=0, padx=3, pady=3)

Button_5 = tk.Button(Button_Frame, text=5, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=5: number_click(a))
Button_5.grid(row=2, column=1, padx=3, pady=3)

Button_6 = tk.Button(Button_Frame, text=6, pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=6: number_click(a))
Button_6.grid(row=2, column=2, padx=3, pady=3)

Button_1 = tk.Button(Button_Frame, text=1, pady=5, padx=10,  width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=1: number_click(a))
Button_1.grid(row=3, column=0, padx=3, pady=3)

Button_2 = tk.Button(Button_Frame, text=2, pady=5, padx=10,  width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=2: number_click(a))
Button_2.grid(row=3, column=1, padx=3, pady=3)

Button_3 = tk.Button(Button_Frame, text=3, pady=5, padx=10,  width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=3: number_click(a))
Button_3.grid(row=3, column=2, padx=3, pady=3)

Button_0 = tk.Button(Button_Frame, text=0, pady=5, padx=10,  width=10, height=4, borderwidth=5, border=5,
                     command=lambda a=0: number_click(a))
Button_0.grid(row=4, column=1, padx=3, pady=3)

Button_dot = tk.Button(Button_Frame, text=".", pady=5, padx=10,  width=10, height=4, borderwidth=5, border=5,
                       command=lambda a=".": dot_click(a))
Button_dot.grid(row=4, column=0, padx=3, pady=3)

Button_equal = tk.Button(Button_Frame, text="=", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                         command=equal_click)
Button_equal.grid(row=4, column=2, padx=3, pady=3)

Button_plus = tk.Button(Button_Frame, text="+", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                        command=plus_click)
Button_plus.grid(row=4, column=3, padx=3, pady=3)

Button_minus = tk.Button(Button_Frame, text="-", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                         command=minus_click)
Button_minus.grid(row=3, column=3, padx=3, pady=3)

Button_multiply = tk.Button(Button_Frame, text="x", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                            command=multiply_click)
Button_multiply.grid(row=2, column=3, padx=3, pady=3)

Button_divide = tk.Button(Button_Frame, text="÷", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                          command=divide_click)
Button_divide.grid(row=1, column=3, padx=3, pady=3)

Button_clear = tk.Button(Button_Frame, text="C", pady=5, padx=10, width=10, height=4, borderwidth=5, border=5,
                         command=clear_all)
Button_clear.grid(row=0, column=3, padx=3, pady=3)

Button_parentheses1 = tk.Button(Button_Frame, text="", pady=5, padx=10,  width=10,
                                height=4, borderwidth=5, border=5, state="disabled")
Button_parentheses1.grid(row=0, column=0, padx=3, pady=3)

Button_parentheses2 = tk.Button(Button_Frame, text="", pady=5, padx=10,  width=10,
                                height=4, borderwidth=5, border=5, state="disabled")
Button_parentheses2.grid(row=0, column=1, padx=3, pady=3)

Button_percent = tk.Button(Button_Frame, text="%", pady=5, padx=10,  width=10,
                           height=4, borderwidth=5, border=5, state="disabled")
Button_percent.grid(row=0, column=2, padx=3, pady=3)

screen.mainloop()
