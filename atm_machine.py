import random

code = []
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
check_if_first_time = input("Is this your first time using ASA ATM's:")
x = 0


user_balances = {
    "Peter": 50,
    "John": 50,
    "Jack": 50,
    "Rachel": 50
}
if check_if_first_time == "yes":
    new_user_name = input("What is your name:")
    while x < 4:
        code.append(random.choice(number))
        x = x + 1.
    print(code)
    user_codes = open("user_data.txt", "a")
    user_codes.write(new_user_name + ": " + str(code))
    user_codes.close()

    print("Your starting balance will be $50.")

elif check_if_first_time == "no":
    user_name = input("What is your name:")
    user_code = int(input("What is your code:"))
    all_users = user_codes.keys()
    for i in all_users:
        if i == user_name:
            break
        else:
            print("There is no user named " + user_name + ". Wait a minute... You are a scammer aren't you. "
                                                          "CALLING 911...")
            break
    code_check = user_codes.get(i)
    if code_check == user_code:
        deposit_or_withdraw = input("Would you like to deposit or withdraw money:")
        if deposit_or_withdraw == "deposit":
            balance_check = user_balances.get(i)
            print("Your current balance is: $" + str(balance_check) + ".")
            amount_to_deposit = int(input("How much would you like to deposit:"))
            user_balances[i] = balance_check + amount_to_deposit
            print("Your updated balance is: $" + str(user_balances.get(i)) + ".")
        elif deposit_or_withdraw == "withdraw":
            balance_check = user_balances.get(i)
            print("Your current balance is: $" + str(balance_check) + ".")
            amount_to_withdraw = int(input("How much would you like to withdraw:"))
            user_balances[i] = balance_check - amount_to_withdraw
            updated_balance = balance_check - amount_to_withdraw
            if updated_balance > 0:
                print("Your updated balance is: $" + str(user_balances.get(i)) + ".")
            else:
                print("You cant withdraw that amount.")

    else:
        print("There is no code " + str(user_code) + ". Wait a minute... You are a scammer aren't you. "
                                                     "CALLING 911...")

else:
    print("Please type in yes or no.")
