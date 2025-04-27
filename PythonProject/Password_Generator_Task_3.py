import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            show_error("Password length must be at least 6 characters.")
            return

        # Make sure at least one letter, one number, and one special character
        password = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Fill the rest of the password
        if length > 3:
            characters = string.ascii_letters + string.digits + string.punctuation
            password += random.choices(characters, k=length - 3)

        random.shuffle(password)
        password = ''.join(password)

        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')

    except ValueError:
        show_error("Please enter a valid number.")

# Function to copy password
def copy_password():
    password = password_display.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        show_info("Password copied to clipboard!")

# Function to show custom error popup with dark mode
def show_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Error")
    error_window.configure(bg="#2C2F33")  # Dark mode background
    error_window.resizable(False, False)

    # Set the desired window size (increased size)
    window_width = 400  # Increase the width (original was 300)
    window_height = 200  # Increase the height (original was 150)
    screen_width = error_window.winfo_screenwidth()
    screen_height = error_window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    error_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Error title label
    lbl = tk.Label(error_window, text="⚠️ Error!", font=("Arial", 18, "bold"), fg="red", bg="#2C2F33")
    lbl.pack(pady=10)

    # Error message label
    msg = tk.Label(error_window, text=message, font=("Arial", 14), fg="white", bg="#2C2F33")
    msg.pack(pady=5)

    # OK button
    btn = tk.Button(error_window, text="OK", font=("Arial", 12), bg="#7289DA", fg="white", command=error_window.destroy)
    btn.pack(pady=10)


# Function to show custom info popup (like messagebox.showinfo)
def show_info(message):
    info_window = tk.Toplevel(root)
    info_window.title("Info")
    info_window.configure(bg="#2C2F33")
    info_window.resizable(False, False)

    # Set window size
    window_width = 300
    window_height = 150
    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    info_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # Info title label
    lbl = tk.Label(info_window, text="✔️ Success!", font=("Arial", 18, "bold"), fg="green", bg="#2C2F33")
    lbl.pack(pady=10)

    # Info message label
    msg = tk.Label(info_window, text=message, font=("Arial", 14), fg="white", bg="#2C2F33")
    msg.pack(pady=5)

    # OK button
    btn = tk.Button(info_window, text="OK", font=("Arial", 12), bg="#7289DA", fg="white", command=info_window.destroy)
    btn.pack(pady=10)

# Centering the window function
def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

# Setting up the GUI
root = tk.Tk()
root.title("Password Generator")
window_width = 450
window_height = 320
center_window(root, window_width, window_height)
root.config(bg="#2C2F33")
root.resizable(False, False)

# Styling
label_font = ("Helvetica", 14)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
fg_color = "#FFFFFF"
btn_color = "#7289DA"
entry_bg = "#23272A"

# Widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#2C2F33", fg=fg_color)
title_label.pack(pady=15)

length_label = tk.Label(root, text="Enter Password Length:", font=label_font, bg="#2C2F33", fg=fg_color)
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=entry_font, width=30, bg=entry_bg, fg=fg_color, insertbackground=fg_color, justify="center")
length_entry.pack(ipady=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", font=button_font, bg=btn_color, fg=fg_color, activebackground="#5B6EAE", command=generate_password)
generate_button.pack(pady=10)

# Password display field
password_display = tk.Entry(root, font=("Helvetica", 13), width=30, bg=entry_bg, fg=fg_color, insertbackground=fg_color, justify="center")
password_display.config(readonlybackground=entry_bg)
password_display.config(state='readonly')
password_display.pack(ipady=7, pady=5)

copy_button = tk.Button(root, text="Copy Password", font=button_font, bg=btn_color, fg=fg_color, activebackground="#5B6EAE", command=copy_password)
copy_button.pack(pady=10)

# Run the application
root.mainloop()
