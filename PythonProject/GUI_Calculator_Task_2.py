import tkinter as tk
from tkinter import Toplevel, Label, Button
import math


def show_error(message):
    error_window = Toplevel(root)
    error_window.title("Error")
    error_window.configure(bg="#ffe6e6")
    error_window.resizable(False, False)

    window_width = 300
    window_height = 150
    screen_width = error_window.winfo_screenwidth()
    screen_height = error_window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    error_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    lbl = Label(error_window, text="⚠️ Error!", font=("Arial", 18, "bold"), fg="red", bg="#ffe6e6")
    lbl.pack(pady=10)

    msg = Label(error_window, text=message, font=("Arial", 14), bg="#ffe6e6")
    msg.pack(pady=5)

    btn = Button(error_window, text="OK", font=("Arial", 12), bg="#ff4d4d", fg="white", command=error_window.destroy)
    btn.pack(pady=10)


def button_click(symbol):
    current = entry_display.get()

    if symbol in ('sin', 'cos', 'tan', '√'):
        try:
            if current == '':
                show_error(f"Enter a number first for {symbol}")
                return

            num = float(current)
            if symbol == 'sin':
                result = math.sin(math.radians(num))
            elif symbol == 'cos':
                result = math.cos(math.radians(num))
            elif symbol == 'tan':
                result = math.tan(math.radians(num))
            elif symbol == '√':
                if num < 0:
                    show_error("Cannot take √ of negative number")
                    return
                result = math.sqrt(num)

            entry_display.delete(0, tk.END)
            entry_display.insert(0, str(result))
        except Exception as e:
            show_error(str(e))
            clear_display()
    else:
        entry_display.insert(tk.END, symbol)


def power_function():
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + "^")  # <<---- Display ^


def clear_display(event=None):
    entry_display.delete(0, tk.END)


def calculate_result(event=None):
    try:
        expression = entry_display.get()
        expression = expression.replace('^', '**')  # <<---- Replace ^ before eval
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except ZeroDivisionError:
        show_error("Cannot divide by zero")
        clear_display()
    except Exception as e:
        show_error("Invalid Input")
        clear_display()


def on_keypress(event):
    key = event.char
    if key in '0123456789.+-*/()^':
        entry_display.insert(tk.END, key)
    elif event.keysym == 'Return':
        calculate_result()
    elif event.keysym == 'BackSpace':
        current = entry_display.get()
        entry_display.delete(0, tk.END)
        entry_display.insert(0, current[:-1])


def on_button_press(btn):
    btn.config(bg="#cccccc")


def on_button_release(btn, color):
    btn.config(bg=color)


# Create main window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#ffffff")

# Center the main window
window_width = 400
window_height = 620
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Entry display
entry_display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#f9f9f9")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button configuration
buttons = [
    ('(', ')', 'Clear', 'xʸ'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('sin', 'cos', 'tan', '√')
]

colors = {
    "number": "#e0e0e0",
    "operator": "#a0c4ff",
    "function": "#ffd6a5",
    "equal": "#b5ead7",
    "clear": "#ffadad",
    "power": "#caffbf",
    "bracket": "#c3bef0"
}

# Create buttons dynamically
for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        if char:
            if char == '=':
                bg_color = colors["equal"]
                action = calculate_result
            elif char == 'Clear':
                bg_color = colors["clear"]
                action = clear_display
            elif char == 'xʸ':
                bg_color = colors["power"]
                action = power_function
            elif char in ('+', '-', '*', '/'):
                bg_color = colors["operator"]
                action = lambda ch=char: button_click(ch)
            elif char in ('sin', 'cos', 'tan', '√'):
                bg_color = colors["function"]
                action = lambda ch=char: button_click(ch)
            elif char in ('(', ')'):
                bg_color = colors["bracket"]
                action = lambda ch=char: button_click(ch)
            else:
                bg_color = colors["number"]
                action = lambda ch=char: button_click(ch)

            btn = tk.Button(root, text=char, font=("Arial", 18), bg=bg_color, relief="groove", bd=2, command=action)
            btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

            # Bind button press/release effect
            btn.bind("<ButtonPress-1>", lambda e, b=btn: on_button_press(b))
            btn.bind("<ButtonRelease-1>", lambda e, b=btn, col=bg_color: on_button_release(b, col))

# Make all columns and rows expand equally
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

# Keyboard bindings
root.bind('<Return>', calculate_result)
root.bind('<BackSpace>', on_keypress)
root.bind('<Key>', on_keypress)

# Start the main event loop
root.mainloop()
