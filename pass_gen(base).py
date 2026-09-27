import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Letters:", letters)
print("Numbers:", numbers)
print("Symbols:", symbols)
