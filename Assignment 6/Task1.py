import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

root = tk.Tk()
root.title("Calculator")
root.geometry("360x480")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

# Display Box
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    font=("Arial", 20),
    textvariable=input_text,
    width=50,
    bd=10,
    relief="ridge",
    justify="right"
)
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

# Buttons Frame
btns_frame = tk.Frame(root)
btns_frame.pack()

# First Row
tk.Button(btns_frame, text="C", width=10, height=3, command=btn_clear).grid(row=1, column=0)
tk.Button(btns_frame, text="/", width=10, height=3, command=lambda: btn_click("/")).grid(row=1, column=1)
tk.Button(btns_frame, text="*", width=10, height=3, command=lambda: btn_click("*")).grid(row=1, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, command=lambda: btn_click("-")).grid(row=1, column=3)

# Second Row
tk.Button(btns_frame, text="7", width=10, height=3, command=lambda: btn_click("7")).grid(row=2, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, command=lambda: btn_click("8")).grid(row=2, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, command=lambda: btn_click("9")).grid(row=2, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, command=lambda: btn_click("+")).grid(row=2, column=3)

# Third Row
tk.Button(btns_frame, text="4", width=10, height=3, command=lambda: btn_click("4")).grid(row=3, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, command=lambda: btn_click("5")).grid(row=3, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, command=lambda: btn_click("6")).grid(row=3, column=2)
tk.Button(btns_frame, text="=", width=10, height=7, command=btn_equal).grid(row=3, column=3, rowspan=2)

# Fourth Row
tk.Button(btns_frame, text="1", width=10, height=3, command=lambda: btn_click("1")).grid(row=4, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, command=lambda: btn_click("2")).grid(row=4, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, command=lambda: btn_click("3")).grid(row=4, column=2)

# Fifth Row
tk.Button(btns_frame, text="0", width=22, height=3, command=lambda: btn_click("0")).grid(row=5, column=0, columnspan=2)
tk.Button(btns_frame, text=".", width=10, height=3, command=lambda: btn_click(".")).grid(row=5, column=2)

root.mainloop()
