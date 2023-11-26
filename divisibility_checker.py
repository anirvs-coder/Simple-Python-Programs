def divide(in_number, in_dividend):
    return in_number % in_dividend == 0


number = float(input("What number would you like to divide:"))
dividend = float(input("What number would you like to divide the other number by:"))
if divide(number, dividend):
    print("This number is divisible.")
else:
    print("This number is not divisible.")