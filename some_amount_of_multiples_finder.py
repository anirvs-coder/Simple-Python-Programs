amount_of_multiples = int(input("How POSITIVE multiples do you want:"))
number_to_find_multiples_of = int(input("What number would you like me to find " + str(amount_of_multiples) + " multiples of:"))
numbers_list = []
numbers = amount_of_multiples
while not numbers == 0:
    amount_of_multiples_left = amount_of_multiples - 1
    numbers_list.append(amount_of_multiples_left)
    numbers = numbers + 1
print(amount_of_multiples_left)