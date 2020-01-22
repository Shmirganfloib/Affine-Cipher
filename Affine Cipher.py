# v1.0
# Created by CamShaft54, Reevak05, and MetalTurtle18

import random

import PySimpleGUI as Sg

cipher_select_layout = [
    [Sg.Text('Select cipher:')],
    [Sg.Radio('Affine Cipher', "cipher_type", key='affine', default=True),
     Sg.Radio('Caesar Cipher', "cipher_type", key='caesar', default=True)],
    [Sg.Button('Submit', bind_return_key=True)]]
window = Sg.Window('Cipher Select', default_element_size=(40, 1)).Layout(cipher_select_layout)


# This function converts characters to decimals
def char_to_num(k):
    z = (ord(char_list[k].lower()) - 97)
    return z


# This function converts decimals to characters
def num_to_char(n):
    m = chr(n + 97)
    return m


while True:
    event, values = window.read()
    if event in (None, 'EXIT'):
        break
    if event == 'Submit':
        affine = values['affine']
        caesar = values['caesar']
        break

if affine:
    affine_layout = [
        [Sg.Radio('Encrypt      ', "caesar_method", default=True, key='encrypt_input'),
         Sg.Radio('Decrypt', "caesar_method", key='decrypt_input')],
        [Sg.Text('Enter operands for encryption/decryption:')],
        [Sg.Text('Multiplier or Divisor:'), Sg.Input(default_text='1', key='multiplier'),
         Sg.Text('Addend or Minuend:'), Sg.Input(default_text='0', key='addend'),
         Sg.Checkbox('Random', default=False, key='random')],
        [Sg.Text('Input:')],
        [Sg.Multiline(size=(70, 5), enter_submits=True, key='code_input', do_not_clear=False)],
        [Sg.Text('Output:')],
        [Sg.Output(size=(110, 10))],
        [Sg.Button('Submit', bind_return_key=True)]]
    window = Sg.Window('Affine Cipher', default_element_size=(40, 1)).Layout(affine_layout)
    result = ""
    select = ""

    # This function multiplies a number then adds a number and returns mod 26 of that
    def mod():
        x = ((int(number_input) * multiplier) + addend) % 26
        return x

    # This function is a modified modular multiplicative inverse
    def modInverse(y):
        for k in range(0, 26):
            if (9 * multiplier) % 26 == ((y - addend) % 26):
                return k
        return k


    while True:
        result = ""
        event, values = window.read()
        if event in (None, 'EXIT'):
            break
        if event == 'Submit':
            multiplier = int(values['multiplier'])
            addend = int(values['addend'])
            random_operand = values['random']
            if random_operand:
                multiplier = random.randint(2, 10)
                addend = random.randint(2, 10)
            print("Multiplier/Divisor = " + str(multiplier))
            print("Addend/Minuend = " + str(addend))
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
if caesar:
    print("work in progress")
    caesar_layout = [
        [Sg.Text('Welcome to Caesar Cipher')],
        [Sg.Radio('Encrypt      ', "caesar_method", default=True, key='encrypt_input'),
         Sg.Radio('Decrypt', "caesar_method", key='decrypt_input')],
        [Sg.Text('Enter key (A, B, C, etc.)'), Sg.Input(default_text='A', key='char_key')],
        [Sg.Text('Input:')],
        [Sg.Multiline(size=(70, 5), enter_submits=True, key='char_input')],
        [Sg.Text('Output:')],
        [Sg.Output(size=(110, 10))],
        [Sg.Button('Submit', bind_return_key=True)]]
    window = Sg.Window('Cipher Select', default_element_size=(40, 1)).Layout(caesar_layout)
    while True:
        result = ""
        event, values = window.read()
        if event in (None, 'EXIT'):
            break
        if event == 'Submit':
            print("work in progress")
window.close()
