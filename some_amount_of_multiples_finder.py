amount_of_multiples = int(input("How POSITIVE multiples do you want:"))
number_to_find_multiples_of = int(input("What number would you like me to find " + str(amount_of_multiples) + "multiples of:"))
numbers_list = []
numbers = amount_of_multiples
numbers_list.append(amount_of_multiples)
while not numbers == 0:
    amount_of_multiples = amount_of_multiples - 1
    numbers_list.append(amount_of_multiples)
    numbers = numbers - 1
numbers_list.reverse()
multiplied_numbers_list = []

for i in numbers_list:
    new_number = i * number_to_find_multiples_of
    multiplied_numbers_list.append(new_number)

total = 0
for i in range(0, len(multiplied_numbers_list)):
    total = total + multiplied_numbers_list[i]
print("Here are the numbers: " + str(multiplied_numbers_list[1:len(multiplied_numbers_list)]) + ".")
print("Here is the sum of the numbers: " + str(total) + ".")