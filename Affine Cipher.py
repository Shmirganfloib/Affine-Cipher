# v0.9
# infinite loop
while 0 == 0:
    result = ""


    # This function is a modified modular multiplicative inverse
    def modInverse(y):
        for x in range(0, 26):
            if (9 * x) % 26 == ((y - 7) % 26):
                return x
        return x


    # input
    select = input("Enter E for encryption or D for decryption: ")
    if select == "E":
        code_input = input("Enter word to be encoded: ")
    elif select == "D":
        code_input = input("Enter word to be decoded: ")
    else:
        code_input = "error"

    if code_input != "error":
        my_list = list(code_input)
        print(len(code_input))
        if select == "E":  # This is the driver code to for encryption
            for i in range(len(code_input)):
                if code_input.isnumeric():
                    number_input = int(code_input)
                else:
                    number_input = (ord(str(my_list[i]).lower()) - 97)
                intresult = ((int(number_input) * 9) + 7) % 26
                result = result + chr(intresult + 97).upper()
                print("\n")
                print("Encoded word is " + result)
        elif select == "D":  # This is the driver code to for decryption
            for i in range(len(code_input)):
                if code_input.isnumeric():
                    number_input = int(code_input)
                else:
                    number_input = (ord(str(my_list[i]).lower()) - 97)
                    print(ord(str(my_list[i]).lower()))
                    print(number_input)
                intresult = modInverse(number_input)
                print("Decoded number is " + str(intresult))
                result = result + chr(intresult + 97).upper()
            print("\n")
            print("Decoded word is " + result)
    else:
        print("Error. Please try again.")
    for i in range(0, 4):
        print("\n")
