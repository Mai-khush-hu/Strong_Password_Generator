import string
import random
import tkinter as tk

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")

include_letters = input("Include letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if include_letters == "y":
    characters += string.ascii_letters

if include_numbers == "y":
    characters += string.digits

if include_symbols == "y":
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your password is:", password)

root = tk.Tk()
root.withdraw()

root.clipboard_clear()
root.clipboard_append(password)
root.update()

print("Password copied to clipboard!")
root.destroy()
