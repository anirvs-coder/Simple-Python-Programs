import math

factorial = int(input("What is the factorial you would like to make into a perfect square: "))
all_numbers_in_factorial = []
changeable_factorial = factorial + 1
while not factorial == 0:
    changeable_factorial = changeable_factorial - 1
    all_numbers_in_factorial.append(changeable_factorial)
    factorial = factorial - 1

total = 1
for i in range(0, len(all_numbers_in_factorial)):
    total = total * all_numbers_in_factorial[i]

prime_factorization = []
while total % 2 == 0:
    prime_factorization.append(2)
    total = total // 2

for i in range(3, int(math.sqrt(total)) + 1, 2):
    while total % i == 0:
        prime_factorization.append(i)
        total = total // i

highest_number = prime_factorization[-1]
amount_of_times_a_number_appears = []
while 1 < highest_number:
    amount_of_times_a_number_appears.append(prime_factorization.count(highest_number))
    highest_number = highest_number - 1

odd_numbers = []
for i in amount_of_times_a_number_appears:
    if (i % 2) == 0:
        break
    else:
        odd_numbers.append(i)
