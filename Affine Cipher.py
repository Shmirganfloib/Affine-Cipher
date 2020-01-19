# v0.9
# infinite loop
import PySimpleGUI as Sg

layout = [[Sg.Text('Welcome to Affine Cipher')],
          [Sg.Text('Select your Cipher Type')],
          [Sg.Radio('My first Radio!     ', "RADIO1", default=True)]]
window = Sg.Window('Affine Cipher', default_element_size=(40, 1)).Layout(layout)
values, event = window.Read()
result = ""


# This function is a modified modular multiplicative inverse
def modInverse(y):
    for k in range(0, 26):
        if (9 * k) % 26 == ((y - 7) % 26):
            return k
    return k


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
                current_character = my_list[i].lower()
                number_input = (ord(current_character) - 97)
            if 0 <= number_input <= 25:
                intresult = ((int(number_input) * 9) + 7) % 26
            else:
                intresult = number_input
            result = result + chr(intresult + 97).upper()
            print(intresult)
        print("Encoded word is " + result)
    elif select == "D":  # This is the driver code to for decryption
        for i in range(len(code_input)):
            if code_input.isnumeric():
                number_input = int(code_input)
            else:
                current_character = my_list[i].lower()
                number_input = (ord(current_character) - 97)
                print(number_input)
            if 0 <= number_input <= 25:
                intresult = modInverse(number_input)
            else:
                intresult = number_input
            print("Decoded number is " + str(intresult))
            result = result + chr(intresult + 97).upper()
        print("\n")
        print("Decoded word is " + result)
else:
    print("Error. Please try again.")
for i in range(0, 4):
    print("\n")
