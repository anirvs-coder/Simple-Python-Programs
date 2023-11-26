import random

code = []
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
check_if_first_time = input("Is this your first time using ASA ATM's:")
x = 0
user_data = {
    "Peter": 6275,
    "John": 2012,
    "Jack": 7242,
    "Rachel": 4489
}
if check_if_first_time == "yes":
    user_name = input("What is your name:")
    while x < 4:
        code.append(random.choice(number))
        x = x + 1.
    print(code)
    user_data.update({user_name: code})

elif check_if_first_time == "no":
    name_check = input("What is your name:")
    code_check = int(input("What is your code:"))
    all_values = user_data.values()
    for i in all_values:
        print(i)

# else: print("There is no code with " + str(code_check) + ". Wait a minute... You are a scammer aren't you. CALLING
# ""911...")

else:
    print("Please type in yes or no.")
