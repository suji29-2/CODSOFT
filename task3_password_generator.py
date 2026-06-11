import random
import string

length = int(input("Enter password length: "))

use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = string.ascii_letters

if use_digits.lower() == "y":
    characters += string.digits

if use_symbols.lower() == "y":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

if length < 8:
    strength = "Weak"
elif length < 12:
    strength = "Medium"
else:
    strength = "Strong"

print("\nGenerated Password:", password)
print("Password Strength:", strength)