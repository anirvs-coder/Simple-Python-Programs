num = int(input("Choose a number:"))
operator = input("Choose an operator:")
num2 = int(input("Choose the second number:"))
keep_going = True
if operator == "*":
    answer = num * num2
    print(answer)
elif operator == "/":
    answer = num / num2
    print(answer)
elif operator == "+":
    answer = num + num2
    print(answer)
elif operator == "-":
    answer = num - num2
    print(answer)
else:
    keep_going = False
while keep_going == True:
    operator = input("Choose an operator:")
    keep_going_num = int(input("Choose the  number:"))
    if operator == "*":
        answer = answer * keep_going_num
        print(answer)
    elif operator == "/":
        answer = answer / keep_going_num
        print(answer)
    elif operator == "+":
        answer = answer + keep_going_num
        print(answer)
    elif operator == "-":
        answer = answer - keep_going_num
        print(answer)
    else:
        keep_going = False