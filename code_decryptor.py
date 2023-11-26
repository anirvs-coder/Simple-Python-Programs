decrypt_or_encrypt = input("Would you like to decrypt or encrypt:")
if decrypt_or_encrypt == "decrypt":
    alphabets = {
        "a": "c",
        "b": "d",
        "c": "e",
        "d": "f",
        "e": "g",
        "f": "h",
        "g": "i",
        "h": "j",
        "i": "k",
        "j": "l",
        "k": "m",
        "l": "n",
        "m": "o",
        "n": "p",
        "o": "q",
        "p": "r",
        "q": "s",
        "r": "t",
        "s": "u",
        "t": "v",
        "u": "w",
        "v": "x",
        "w": "y",
        "x": "z",
        "y": "a",
        "z": "b",
        " ": ",",
        ",": " "
    }

    decrypted_code = []
    code_to_decrypt = input("What is the code you would like to decrypt:")
    for i in code_to_decrypt:
        if i in alphabets:
            decrypted_code.append(alphabets[i])

    print("".join(decrypted_code))

elif decrypt_or_encrypt == "encrypt":
    alphabets = {
        "c": "a",
        "d": "b",
        "e": "c",
        "f": "d",
        "g": "e",
        "h": "f",
        "i": "g",
        "j": "h",
        "k": "i",
        "l": "j",
        "m": "k",
        "n": "l",
        "o": "m",
        "p": "n",
        "q": "o",
        "r": "p",
        "s": "q",
        "t": "r",
        "u": "s",
        "v": "t",
        "w": "u",
        "x": "v",
        "y": "w",
        "z": "x",
        "a": "y",
        "b": "z",
        " ": ",",
        ",": " "
    }

    encrypted_code = []
    code_to_encrypt = input("What is the code you would like to encrypt:")
    for i in code_to_encrypt:
        if i in alphabets:
            encrypted_code.append(alphabets[i])

    print("".join(encrypted_code))
