# v0.9
# infinite loop
import PySimpleGUI as Sg

setup_layout = [[Sg.Text('Welcome to Affine Cipher')],
                [Sg.Text('Select your Cipher Type')],
                [Sg.Radio('Affine Cipher', "cipher_type", default=True)],
                [Sg.Radio('Encrypt      ', "method", default=True, key='encrypt_input'),
                 Sg.Radio('Decrypt', "method", key='decrypt_input')],
                [Sg.Text('Enter Text:'), Sg.Input(key='code_input')],
                [Sg.Button('Submit')]]
window = Sg.Window('Affine Cipher', default_element_size=(40, 1)).Layout(setup_layout)
result = ""
select = ""
while True:
    event, values = window.read()
    if event in (None, 'Submit'):  # if user closes window or clicks cancel
        code_input = str(values['code_input'])
        if values['encrypt_input']:
            select = "E"
        elif values['decrypt_input']:
            select = "D"
        print(code_input)
        break


# This function is a modified modular multiplicative inverse
def modInverse(y):
    for k in range(0, 26):
        if (9 * k) % 26 == ((y - 7) % 26):
            return k
    return k


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
    print("Decoded word is " + result)
