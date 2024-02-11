read_or_write = input("Would you ike to read or write(r or w)")
if read_or_write == "r":
    user_name = input("Which user would you like to see the code of:")
    file = open("data.txt", "r")
    for i in file:
        user_list = i.split(":")
        if user_list[0] == user_name:
            print(user_list[1])
            break
        else:
            break
elif read_or_write == "w":
    new_user_name = input("What is your name:")
    new_user_code = int(input("What is your code:"))
    file_writing = open("data.txt", "a")
    file_writing.write(new_user_name + ":" + str(new_user_code) + "\n")
    file_writing.close()

