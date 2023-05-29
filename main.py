import tkinter as tk
first_number = 0.0
second_number = 0.0
calculation = ""
equal_clickable = True
equal_clickable_2 = True
no_number = True
string_on = False
calculation_on = False
BG = "#BFBFBF"
CAL_BG = "#DCDCDC"
CAL_CLICKED_BG = "#B6FFA3"

screen = tk.Tk()
screen.configure(bg="white")
screen.title("Calculator")

calculator_frame = tk.Frame(screen, bg=BG, padx=15, pady=15, relief="raised", border=12)
calculator_frame.pack()

display = tk.Entry(calculator_frame, width=18, font=("times new roman", 40), state="disabled",
                   disabledbackground="white", disabledforeground="black", relief="sunken", border=8)
display.pack(pady=5, padx=5)


def button_bg_clear():
    Button_multiply.config(bg=CAL_BG)
    Button_plus.config(bg=CAL_BG)
    Button_divide.config(bg=CAL_BG)
    Button_percent.config(bg=CAL_BG)
    Button_minus.config(bg=CAL_BG)


def factorial_calculation(f):
    if f == 0:
        return 1
    else:
        return f * factorial_calculation(f-1)


def factorial():
    global equal_clickable, string_on
    try:
        n = float(display.get())
        int_number = int(n)
        display["state"] = "normal"
        display.delete(0, tk.END)
        if n == int_number:
            n = int(n)
            if 170 >= n >= 0:
                num = factorial_calculation(n)
                display.insert(tk.END, num)
            elif n > 170:
                display.insert(tk.END, "INF!!")
                equal_clickable = False
                string_on = True
            else:
                display.insert(tk.END, "Negative Number!!")
                equal_clickable = False
                string_on = True
        else:
            display.insert(tk.END, "Float Number!")
            equal_clickable = False
            string_on = True
        display["state"] = "disabled"
    except ValueError:
        pass


def number_click(x):
    global equal_clickable, no_number, string_on, calculation_on
    display["state"] = "normal"
    if calculation_on:
        display.delete(0, tk.END)
        calculation_on = False
    if not equal_clickable:
        display.delete(0, tk.END)
        equal_clickable = True
        string_on = False
    display.insert(tk.END, x)
    display["state"] = "disabled"
    no_number = False


def dot_click(x):
    if "." in display.get():
        pass
    else:
        global equal_clickable, string_on, calculation_on
        display["state"] = "normal"
        if calculation_on:
            display.delete(0, tk.END)
            calculation_on = False
        if not equal_clickable:
            display.delete(0, tk.END)
            equal_clickable = True
            string_on = False
        display.insert(tk.END, x)
        display["state"] = "disabled"


def prc_click(prc):
    global first_number, calculation, equal_clickable_2, calculation_on
    if no_number or string_on or calculation == prc:
        pass
    elif calculation == "":
        first_number = display.get()
        if prc == "*":
            Button_multiply.config(bg=CAL_CLICKED_BG)
        elif prc == "/":
            Button_divide.config(bg=CAL_CLICKED_BG)
        elif prc == "%":
            Button_percent.config(bg=CAL_CLICKED_BG)
        else:
            Button_plus.config(bg=CAL_CLICKED_BG)
        calculation = prc
        equal_clickable_2 = True
        calculation_on = True
    else:
        calculation = prc
        if prc == "*":
            button_bg_clear()
            Button_multiply.config(bg=CAL_CLICKED_BG)
        elif prc == "/":
            button_bg_clear()
            Button_divide.config(bg=CAL_CLICKED_BG)
        elif prc == "%":
            button_bg_clear()
            Button_percent.config(bg=CAL_CLICKED_BG)
        else:
            button_bg_clear()
            Button_plus.config(bg=CAL_CLICKED_BG)


def minus_click():
    global first_number, calculation, equal_clickable_2, calculation_on
    display["state"] = "normal"
    if calculation_on:
        display.delete(0, tk.END)
        display.insert(0, "-")
        calculation_on = False
    elif len(display.get()) == 0:
        display.insert(0, "-")
    else:
        if no_number or string_on or calculation == "-":
            pass
        elif calculation == "":
            first_number = display.get()
            Button_minus.config(bg=CAL_CLICKED_BG)
            calculation = "-"
            equal_clickable_2 = True
            calculation_on = True
        else:
            calculation = "-"
            button_bg_clear()
            Button_minus.config(bg=CAL_CLICKED_BG)
    display["state"] = "disabled"


def equal_click():
    global equal_clickable, equal_clickable_2, second_number, calculation, calculation_on, string_on
    if equal_clickable and equal_clickable_2 and not first_number == 0.0:
        try:
            global second_number, calculation
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
            elif calculation == "%":
                math = float(first_number) * float(second_number) / 100
            if math == int(math):
                math = int(math)
            display.insert(0, math)
            display["state"] = "disabled"
            calculation = ""
            calculation_on = False
            button_bg_clear()
            equal_clickable = False
            equal_clickable_2 = False
            second_number = 0.0
        except ValueError:
            pass
        except ZeroDivisionError:
            clear_all()
            display["state"] = "normal"
            display.insert(tk.END, "Zero Division!!")
            display["state"] = "disabled"
            string_on = True
            equal_clickable = False
    else:
        pass


def clear_all():
    global first_number, second_number, display, calculation
    global equal_clickable, no_number, string_on, calculation_on
    first_number = 0.0
    second_number = 0.0
    calculation = ""
    calculation_on = False
    display["state"] = "normal"
    display.delete(0, tk.END)
    display["state"] = "disabled"
    equal_clickable = True
    no_number = True
    string_on = False
    button_bg_clear()


def clear():
    if string_on:
        clear_all()
    else:
        display["state"] = "normal"
        display.delete(len(display.get())-1, tk.END)
        display["state"] = "disabled"


Button_Frame = tk.Frame(calculator_frame, bg=BG)
Button_Frame.pack(padx=10, pady=10)

button_list = [7, 8, 9, 4, 5, 6, 1, 2, 3]

for i, number in enumerate(button_list):
    Button = tk.Button(Button_Frame, text=number, width=6, height=2,
                       font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                       command=lambda a=number: number_click(a), bg="#F6F6F6")
    Button.grid(row=i//3 + 1, column=i % 3, padx=3, pady=3)

Button_dot = tk.Button(Button_Frame, text=".", width=6, height=2,
                       font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                       command=lambda a=".": dot_click(a), bg="#F6F6F6")
Button_dot.grid(row=4, column=0, padx=3, pady=3)

Button_0 = tk.Button(Button_Frame, text=0, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=0: number_click(a), bg="#F6F6F6")
Button_0.grid(row=4, column=1, padx=3, pady=3)

Button_equal = tk.Button(Button_Frame, text="=", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=equal_click, bg="#187DFF")
Button_equal.grid(row=4, column=2, padx=3, pady=3)

Button_plus = tk.Button(Button_Frame, text="+", width=6, height=2,
                        font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                        command=lambda a="+": prc_click(a), bg=CAL_BG)
Button_plus.grid(row=4, column=3, padx=3, pady=3)

Button_minus = tk.Button(Button_Frame, text="-", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=minus_click, bg=CAL_BG)
Button_minus.grid(row=3, column=3, padx=3, pady=3)

Button_multiply = tk.Button(Button_Frame, text="x", width=6, height=2,
                            font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                            command=lambda a="*": prc_click(a), bg=CAL_BG)
Button_multiply.grid(row=2, column=3, padx=3, pady=3)

Button_divide = tk.Button(Button_Frame, text="÷", width=6, height=2,
                          font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                          command=lambda a="/": prc_click(a), bg=CAL_BG)
Button_divide.grid(row=1, column=3, padx=3, pady=3)

Button_clear_all = tk.Button(Button_Frame, text="CA", width=6, height=2,
                             font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                             command=clear_all, bg="#DCDCDC")
Button_clear_all.grid(row=0, column=3, padx=3, pady=3)

Button_clear = tk.Button(Button_Frame, text="C", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=clear, bg="#DCDCDC")
Button_clear.grid(row=0, column=0, padx=3, pady=3)

Button_factorial = tk.Button(Button_Frame, text="n!", width=6, height=2,
                             font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                             bg="#DCDCDC", command=factorial)
Button_factorial.grid(row=0, column=1, padx=3, pady=3)

Button_percent = tk.Button(Button_Frame, text="%", width=6, height=2,
                           font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                           bg=CAL_BG, command=lambda a="%": prc_click(a))
Button_percent.grid(row=0, column=2, padx=3, pady=3)

screen.mainloop()
