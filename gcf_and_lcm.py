amount_of_numbers = int(input("How many numbers would you like to find the GCF and LCM of:"))
if amount_of_numbers <= 1:
    print("You must have 2+ numbers")
    breakpoint()
elif amount_of_numbers > 10:
    print("You must have less than 10 numbers")
    breakpoint()

x = 0
all_numbers = []
while x < amount_of_numbers:
    number = int(input("What is your first number:"))
    all_numbers.append(number)
    x = x + 1



