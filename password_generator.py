import random

password_length = int(input("What length do you want your password:"))

start_number_inclusive = False
set_number_inclusive = input("Do you want your password to include numbers:")
if set_number_inclusive == "yes":
    start_number_inclusive = True


start_letter_inclusive = False
set_letter_inclusive = input("Do you want your password to include letters:")
if set_letter_inclusive == "yes":
    start_letter_inclusive = True


start_symbol_inclusive = False
set_symbol_inclusive = input("Do you want your password to include symbols which are _,@,#,!:")
if set_symbol_inclusive == "yes":
    start_symbol_inclusive = True

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letters = ["a", "b", "c", 'd', "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
placeholder = 0
password_items = []

order = [1, 2, 3]

while password_length > placeholder:
    randomized_order = random.choice(order)
    if randomized_order == 1:
        if start_number_inclusive and password_length > placeholder:
            password_items.append(random.choice(numbers))
            placeholder = placeholder + 1
    if randomized_order == 2:
        if start_letter_inclusive and password_length > placeholder:
            password_items.append(random.choice(letters))
            placeholder = placeholder + 1
    if randomized_order == 3:
        if start_symbol_inclusive and password_length > placeholder:
            password_items.append(random.choice(symbols))
            placeholder = placeholder + 1


print("".join(password_items))
