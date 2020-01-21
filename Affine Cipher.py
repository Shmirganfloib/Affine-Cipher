# v1.0
# Created by CamShaft54, Reevak05, and MetalTurtle18

import PySimpleGUI as Sg

# uncomment the lines below when we add additional ciphers
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


# This function converts characters to decimals
def char_to_num(k):
    z = (ord(char_list[k].lower()) - 97)
    return z


# This function multiplies a number then adds a number and returns mod 26 of that
def mod():
    x = ((int(number_input) * 9) + 7) % 26
    return x


# This function is a modified modular multiplicative inverse
def modInverse(y):
    for k in range(0, 26):
        if (9 * k) % 26 == ((y - 7) % 26):
            return k
    return k


# This function converts decimals to characters
def num_to_char(n):
    m = chr(n + 97)
    return m


while True:
    result = ""
    event, values = window.read()
    if event in (None, 'EXIT'):
        break
    if event == 'Submit':
        code_input = str(values['code_input'])
        char_list = list(code_input)
        if values['encrypt_input']:  # Driver code for encryption
            for i in range(len(code_input)):
                if code_input.isnumeric():
                    number_input = int(code_input)
                else:
                    number_input = char_to_num(i)
                if 0 <= number_input <= 25:
                    intresult = mod()
                else:
                    intresult = number_input
                result += num_to_char(intresult).upper()
            print("Your encoded message is: " + result)
        elif values['decrypt_input']:  # Driver code for decryption
            for i in range(len(code_input)):
                if code_input.isnumeric():
                    number_input = int(code_input)
                else:
                    number_input = (ord(char_list[i].lower()) - 97)
                if 0 <= number_input <= 25:
                    intresult = modInverse(number_input)
                else:
                    intresult = number_input
                result += num_to_char(intresult).capitalize()
            print("Your decoded message is: " + result)
window.close()