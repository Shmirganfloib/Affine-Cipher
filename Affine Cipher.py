# v0.9

result = ""

# This function is a modified modular multiplicative inverse
def modInverse(y):
    for x in range(0, 26):
        if (9 * x) % 26 == ((y - 7) % 26):
            return x
    return x


select = input("Type E for encryption and D for decryption")
code_input = input("Enter the Word")

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
        print(result)
elif select == "D":  # This is the driver code to for decryption
    for i in range(len(code_input)):
        if code_input.isnumeric():
            number_input = int(code_input)
        else:
            number_input = (ord(str(my_list[i]).lower()) - 97)
            print(ord(str(my_list[i]).lower()))
            print(number_input)
        intresult = modInverse(number_input)
        print("Decoded Number is " + str(intresult))
        result = result + chr(intresult + 97).upper()
    print("Decoded Word is " + result)
