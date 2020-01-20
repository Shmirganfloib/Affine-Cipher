# v0.9

import PySimpleGUI as Sg

# uncomment the lines below when we add additonal ciphers
setup_layout = [  # [Sg.Text('Welcome to Affine Cipher')],
    # [Sg.Text('Select your Cipher Type')],
    # [Sg.Radio('Affine Cipher', "cipher_type", default=True)],
    [Sg.Radio('Encrypt      ', "method", default=True, key='encrypt_input'),
     Sg.Radio('Decrypt', "method", key='decrypt_input')],
    [Sg.Text('Input:')],
    [Sg.Multiline(size=(70, 5), enter_submits=True, key='code_input', do_not_clear=False)],
    [Sg.Text('Output:')],
    [Sg.Output(size=(110, 10), )],
    [Sg.Button('Submit', bind_return_key=True)]]
window = Sg.Window('Affine Cipher', default_element_size=(40, 1)).Layout(setup_layout)
result = ""
select = ""


# This function is a modified modular multiplicative inverse
def modInverse(y):
    for k in range(0, 26):
        if (9 * k) % 26 == ((y - 7) % 26):
            return k
    return k


while True:
    result = ""
    event, values = window.read()
    if event in (None, 'EXIT'):
        break
    if event == 'Submit':
        code_input = str(values['code_input'])
        my_list = list(code_input)
        if values['encrypt_input']:
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
                result += chr(intresult + 97).upper()
            print("Your Encoded Message is " + result)
        elif values['decrypt_input']:
            for i in range(len(code_input)):
                if code_input.isnumeric():
                    number_input = int(code_input)
                else:
                    current_character = my_list[i].lower()
                    number_input = (ord(current_character) - 97)
                if 0 <= number_input <= 25:
                    intresult = modInverse(number_input)
                else:
                    intresult = number_input
                result += chr(intresult + 97).capitalize()
            print("Your Decoded Message is " + result)
window.close()
