result = "Result is "


def modInverse(a, y):
    a = a % 26
    for x in range(0, 26):
        if ((a * x) % 26) + 7 == y:
            return x
    return x


Decode = input("decode")
print(modInverse(9, Decode))

select = input("Type E for encryption and D for decryption")
code_input = input("Enter the Word")
my_list = list(code_input)
print(len(code_input))
if select == "E":
    for i in range(len(code_input)):
        if code_input.isnumeric():
            number_input = int(code_input)
        else:
            number_input = (ord(str(my_list[i]).lower()) - 97)
        intresult = ((int(number_input) * 9) + 7) % 26
        result = result + chr(intresult + 97).upper()
        print(result)
elif select == "D":
    for i in range(len(code_input)):
        if code_input.isnumeric():
            number_input = int(code_input)
        else:
            number_input = (ord(str(my_list[i]).lower()) - 97)
        intresult = modInverse(9, number_input)
        print("Decoded Number is " + str(intresult))
        result = result + chr(intresult + 97).upper()
    print("Decoded Word is " + str(result))
