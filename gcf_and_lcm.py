def find_gcf(x, y):
    while (y):
        x, y = y, x % y

    return x


which_one = input("Would you like to find the GCF or LCM of your specified numbers:")
numbers = []
how_many_nums = int(input("How many numbers would you like to use:"))
if how_many_nums < 2:
    print("That is not enough numbers.")
else:
    x = 0
    while how_many_nums > x:
        number = int(input("What is the number:"))
        numbers.append(number)
        x = x + 1

    if which_one == "gcf" or "GCF":
        num1 = numbers[0]
        num2 = numbers[1]
        gcf = find_gcf(num1, num2)

        for i in range(2, len(numbers)):
            gcf = find_gcf(gcf, numbers[i])

        print(gcf)
    elif which_one == "lcm" or "LCM":
        print()
    else:
        print()
