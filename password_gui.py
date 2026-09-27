
import tkinter as tk
from tkinter import messagebox
import string
import random


def generate_password():
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())

        if length <= 0 or count <= 0:
            messagebox.showerror(
                "Error",
                "Length and number of passwords must be positive."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror(
            "Error",
            "Select at least one character type."
        )
        return

    # Clear previous passwords
    output_text.delete("1.0", tk.END)

    # Generate multiple passwords
    for i in range(count):
        password = ""

        for j in range(length):
            password += random.choice(characters)

        output_text.insert(
            tk.END,
            f"{i + 1}. {password}\n"
        )


def copy_all():
    passwords = output_text.get("1.0", tk.END).strip()

    if passwords == "":
        messagebox.showwarning(
            "Warning",
            "Generate passwords first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(passwords)
    root.update()

    messagebox.showinfo(
        "Copied",
        "All passwords copied to clipboard!"
    )


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title("🔐 Password Generator")
root.geometry("600x650")
root.resizable(False, False)


# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Create secure random passwords",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 20))


# =========================
# SETTINGS FRAME
# =========================

settings_frame = tk.LabelFrame(
    root,
    text="Password Settings",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=15
)

settings_frame.pack(
    padx=30,
    fill="x"
)


# Password length

length_label = tk.Label(
    settings_frame,
    text="Password Length:",
    font=("Arial", 11)
)

length_label.grid(
    row=0,
    column=0,
    sticky="w",
    pady=8
)


length_entry = tk.Entry(
    settings_frame,
    width=10,
    font=("Arial", 11)
)

length_entry.grid(
    row=0,
    column=1,
    padx=15
)

length_entry.insert(0, "12")


# Number of passwords

count_label = tk.Label(
    settings_frame,
    text="Number of Passwords:",
    font=("Arial", 11)
)

count_label.grid(
    row=1,
    column=0,
    sticky="w",
    pady=8
)


count_entry = tk.Entry(
    settings_frame,
    width=10,
    font=("Arial", 11)
)

count_entry.grid(
    row=1,
    column=1,
    padx=15
)

count_entry.insert(0, "5")


# =========================
# CHARACTER OPTIONS
# =========================

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


letters_check = tk.Checkbutton(
    settings_frame,
    text="Letters (A-Z, a-z)",
    variable=letters_var,
    font=("Arial", 10)
)

letters_check.grid(
    row=2,
    column=0,
    sticky="w",
    pady=5
)


numbers_check = tk.Checkbutton(
    settings_frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial", 10)
)

numbers_check.grid(
    row=3,
    column=0,
    sticky="w",
    pady=5
)


symbols_check = tk.Checkbutton(
    settings_frame,
    text="Symbols (! @ # $ %)",
    variable=symbols_var,
    font=("Arial", 10)
)

symbols_check.grid(
    row=4,
    column=0,
    sticky="w",
    pady=5
)


# =========================
# GENERATE BUTTON
# =========================

generate_button = tk.Button(
    root,
    text="⚡ GENERATE PASSWORDS",
    command=generate_password,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)

generate_button.pack(pady=20)


# =========================
# OUTPUT FRAME
# =========================

output_frame = tk.LabelFrame(
    root,
    text="Generated Passwords",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

output_frame.pack(
    padx=30,
    fill="both",
    expand=True
)


output_text = tk.Text(
    output_frame,
    height=10,
    width=55,
    font=("Consolas", 11),
    wrap="none"
)

output_text.pack(
    fill="both",
    expand=True
)


# =========================
# COPY BUTTON
# =========================

copy_button = tk.Button(
    root,
    text="📋 COPY ALL PASSWORDS",
    command=copy_all,
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
)

copy_button.pack(pady=15)


# =========================
# RUN APPLICATION
# =========================

root.mainloop()