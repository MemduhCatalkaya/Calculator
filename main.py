import tkinter as tk
first_number = 0.0
second_number = 0.0
calculation = ""
equal = True
no_number = True

screen = tk.Tk()
screen.configure(bg="white")

display = tk.Entry(width=18, font=("times new roman", 40), state="disabled",
                   disabledbackground="white", disabledforeground="black")
display.pack(pady=5, padx=5)

info_frame = tk.Frame(bg="white")
info_frame.pack()

display_fn = tk.Entry(info_frame, width=10, font=("times new roman", 30), state="disabled",
                      disabledbackground="#EEEEEE", disabledforeground="black")
display_fn.grid(row=0, column=0, padx=3, pady=3)
display_cal = tk.Entry(info_frame, width=2, font=("times new roman", 20), state="disabled",
                       disabledbackground="#EEEEEE", disabledforeground="black")
display_cal.grid(row=0, column=1, padx=3, pady=3)
display_sn = tk.Entry(info_frame, width=10, font=("times new roman", 30), state="disabled",
                      disabledbackground="#EEEEEE", disabledforeground="black")
display_sn.grid(row=0, column=2, padx=3, pady=3)


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
        display_sn["state"] = "normal"
        display_sn.delete(0, tk.END)
        display_sn["state"] = "disabled"
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


def prc_click(prc):
    if no_number:
        pass
    else:
        global first_number
        global calculation
        if calculation == prc:
            pass
        elif calculation == "":
            first_number = display.get()
            display_fn["state"] = "normal"
            display_fn.delete(0, tk.END)
            display_fn.insert(0, first_number)
            display_fn["state"] = "disabled"
            display_cal["state"] = "normal"
            display_cal.delete(0, tk.END)
            if prc == "*":
                display_cal.insert(0, "X")
            elif prc == "/":
                display_cal.insert(0, "÷")
            elif prc == "%":
                display_cal.insert(0, "%")
            else:
                display_cal.insert(0, "+")
            display_cal["state"] = "disabled"
            display["state"] = "normal"
            display.delete(0, tk.END)
            display["state"] = "disabled"
            calculation = prc
            display_sn["state"] = "normal"
            display_sn.delete(0, tk.END)
            display_sn["state"] = "disabled"
        else:
            calculation = prc
            display_cal["state"] = "normal"
            display_cal.delete(0, tk.END)
            if prc == "*":
                display_cal.insert(0, "X")
            elif prc == "/":
                display_cal.insert(0, "÷")
            elif prc == "%":
                display_cal.insert(0, "%")
            else:
                display_cal.insert(0, "+")
            display_cal["state"] = "disabled"


def minus_click():
    if len(display.get()) == 0:
        display["state"] = "normal"
        display.insert(0, "-")
        display["state"] = "disabled"
    else:
        if no_number:
            pass
        else:
            global first_number
            global calculation
            if calculation == "-":
                pass
            elif calculation == "":
                first_number = display.get()
                display_fn["state"] = "normal"
                display_fn.delete(0, tk.END)
                display_fn.insert(0, first_number)
                display_fn["state"] = "disabled"
                display_cal["state"] = "normal"
                display_cal.delete(0, tk.END)
                display_cal.insert(0, "-")
                display_cal["state"] = "disabled"
                display["state"] = "normal"
                display.delete(0, tk.END)
                display["state"] = "disabled"
                calculation = "-"
                display_sn["state"] = "normal"
                display_sn.delete(0, tk.END)
                display_sn["state"] = "disabled"
            else:
                calculation = "-"
                display_cal["state"] = "normal"
                display_cal.delete(0, tk.END)
                display_cal.insert(0, "-")
                display_cal["state"] = "disabled"


def equal_click():
    global equal
    if not equal:
        pass
    else:
        if first_number == 0:
            pass
        else:
            try:
                global second_number
                global calculation
                equal = False
                math = ""
                second_number = display.get()
                display_sn["state"] = "normal"
                display_sn.delete(0, tk.END)
                display_sn.insert(0, second_number)
                display_sn["state"] = "disabled"
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
                display.insert(0, math)
                display["state"] = "disabled"
                calculation = ""
                second_number = 0.0
                display_cal["state"] = "normal"
                display_cal.delete(0, tk.END)
                display_cal["state"] = "disabled"
            except ValueError:
                pass


def clear_all():
    global first_number, second_number, display, calculation
    global equal, no_number
    first_number = 0.0
    second_number = 0.0
    calculation = ""
    display_cal["state"] = "normal"
    display_cal.delete(0, tk.END)
    display_cal["state"] = "disabled"
    display_sn["state"] = "normal"
    display_sn.delete(0, tk.END)
    display_sn["state"] = "disabled"
    display_fn["state"] = "normal"
    display_fn.delete(0, tk.END)
    display_fn["state"] = "disabled"
    display["state"] = "normal"
    display.delete(0, tk.END)
    display["state"] = "disabled"
    equal = True
    no_number = True


Button_Frame = tk.Frame(screen, bg="white")
Button_Frame.pack(padx=10, pady=10)

Button_7 = tk.Button(Button_Frame, text=7, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=7: number_click(a), bg="#F6F6F6")
Button_7.grid(row=1, column=0, padx=3, pady=3)

Button_8 = tk.Button(Button_Frame, text=8, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=8: number_click(a), bg="#F6F6F6")
Button_8.grid(row=1, column=1, padx=3, pady=3)

Button_9 = tk.Button(Button_Frame, text=9, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=9: number_click(a), bg="#F6F6F6")
Button_9.grid(row=1, column=2, padx=3, pady=3)

Button_4 = tk.Button(Button_Frame, text=4, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=4: number_click(a), bg="#F6F6F6")
Button_4.grid(row=2, column=0, padx=3, pady=3)

Button_5 = tk.Button(Button_Frame, text=5, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=5: number_click(a), bg="#F6F6F6")
Button_5.grid(row=2, column=1, padx=3, pady=3)

Button_6 = tk.Button(Button_Frame, text=6, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=6: number_click(a), bg="#F6F6F6")
Button_6.grid(row=2, column=2, padx=3, pady=3)

Button_1 = tk.Button(Button_Frame, text=1, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=1: number_click(a), bg="#F6F6F6")
Button_1.grid(row=3, column=0, padx=3, pady=3)

Button_2 = tk.Button(Button_Frame, text=2, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=2: number_click(a), bg="#F6F6F6")
Button_2.grid(row=3, column=1, padx=3, pady=3)

Button_3 = tk.Button(Button_Frame, text=3, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=3: number_click(a), bg="#F6F6F6")
Button_3.grid(row=3, column=2, padx=3, pady=3)

Button_0 = tk.Button(Button_Frame, text=0, width=6, height=2,
                     font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                     command=lambda a=0: number_click(a), bg="#F6F6F6")
Button_0.grid(row=4, column=1, padx=3, pady=3)

Button_dot = tk.Button(Button_Frame, text=".", width=6, height=2,
                       font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                       command=lambda a=".": dot_click(a), bg="#F6F6F6")
Button_dot.grid(row=4, column=0, padx=3, pady=3)

Button_equal = tk.Button(Button_Frame, text="=", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=equal_click, bg="#187DFF")
Button_equal.grid(row=4, column=2, padx=3, pady=3)

Button_plus = tk.Button(Button_Frame, text="+", width=6, height=2,
                        font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                        command=lambda a="+": prc_click(a), bg="#DCDCDC")
Button_plus.grid(row=4, column=3, padx=3, pady=3)

Button_minus = tk.Button(Button_Frame, text="-", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=minus_click, bg="#DCDCDC")
Button_minus.grid(row=3, column=3, padx=3, pady=3)

Button_multiply = tk.Button(Button_Frame, text="x", width=6, height=2,
                            font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                            command=lambda a="*": prc_click(a), bg="#DCDCDC")
Button_multiply.grid(row=2, column=3, padx=3, pady=3)

Button_divide = tk.Button(Button_Frame, text="÷", width=6, height=2,
                          font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                          command=lambda a="/": prc_click(a), bg="#DCDCDC")
Button_divide.grid(row=1, column=3, padx=3, pady=3)

Button_clear = tk.Button(Button_Frame, text="C", width=6, height=2,
                         font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                         command=clear_all, bg="#DCDCDC")
Button_clear.grid(row=0, column=3, padx=3, pady=3)

Button_parentheses1 = tk.Button(Button_Frame, text="", width=6, height=2,
                                font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                                state="disabled", bg="#DCDCDC")
Button_parentheses1.grid(row=0, column=0, padx=3, pady=3)

Button_parentheses2 = tk.Button(Button_Frame, text="", width=6, height=2,
                                font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                                state="disabled", bg="#DCDCDC")
Button_parentheses2.grid(row=0, column=1, padx=3, pady=3)

Button_percent = tk.Button(Button_Frame, text="%", width=6, height=2,
                           font=("times new roman", 18, "bold"), borderwidth=5, border=5,
                           bg="#DCDCDC", command=lambda a="%": prc_click(a))
Button_percent.grid(row=0, column=2, padx=3, pady=3)

screen.mainloop()
