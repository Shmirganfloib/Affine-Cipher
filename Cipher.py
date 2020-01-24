# v1.0
# Created by CamShaft54, Reevak05, and MetalTurtle18
import random

import PySimpleGUI as Sg

Sg.theme('TealMono')  # Set PySimpleGUI to "TealMono"
cipher_select_layout = [  # PySimpleGUI layout for cipher setup window
    [Sg.Text('Select cipher:')],
    [Sg.Radio('Affine Cipher', "cipher_type", key='affine', default=False),
     Sg.Radio('Caesar Cipher', "cipher_type", key='caesar', default=False),
     Sg.Radio('Encrypt/Decrypt with Key', "cipher_type", key='key', default=False)],
    [Sg.Button('Submit', bind_return_key=True)]]
# Create window from layout
window = Sg.Window('Cipher Select', default_element_size=(40, 1)).Layout(cipher_select_layout)
affine = False
caesar = False
key = False

# This function converts characters to decimals
def char_to_num(k):
    z = (ord(k.lower()) - 97)
    return z


# This function multiplies a number then adds a number and returns mod 26 of that
def mod():
    x = ((int(number_input) * multiplier) + addend) % 26
    return x


# This function is a modified modular multiplicative inverse
def modInverse(y):
    k = 0
    for k in range(0, 26):
        if (multiplier * k) % 26 == ((y - addend) % 26):
            return k
    return k
  
  
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
        key = values['key']
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
                        number_input = char_to_num(char_list[i])
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
    caesar_layout = [
        [Sg.Text('Welcome to Caesar Cipher')],
        [Sg.Radio('Encrypt      ', "caesar_method", default=True, key='caesar_encrypt'),
         Sg.Radio('Decrypt', "caesar_method", key='caesar_decrypt')],
        [Sg.Text('Key: Decrypted A -->'),
         Sg.Slider(range=(0, 25), orientation='h', size=(33, 20), default_value=0, key='num_key')],
        [Sg.Text('Input:')],
        [Sg.Multiline(size=(70, 5), enter_submits=True, key='char_input')],
        [Sg.Text('Output:')],
        [Sg.Output(size=(70, 10))],
        [Sg.Button('Submit', bind_return_key=True)]]
    window = Sg.Window('Cipher Select', default_element_size=(40, 1)).Layout(caesar_layout)


    def caesar_unshift(p):
        shift_output = (p + num_key) % 26
        return shift_output


    def caesar_shift(q):
        unshift_output = (q - num_key) % 26
        return unshift_output


    while True:
        event, values = window.read()
        num_key = int(values['num_key'])
        caesar_encrypt = values['caesar_encrypt']
        caesar_decrypt = values['caesar_decrypt']
        result = ""
        if event in (None, 'EXIT'):
            break
        if event == 'Submit':
            char_input = values['char_input']
            char_input_list = list(char_input)
            if caesar_encrypt:
                for i in range(len(char_input)):
                    if char_input_list[i].isnumeric():
                        num_input = int(char_input_list[i])
                    else:
                        num_input = char_to_num(char_input_list[i])
                    if 0 <= num_input <= 25:
                        intresult = caesar_shift(num_input)
                        intresult = num_to_char(intresult)
                    elif num_input == -65:
                        intresult = " "
                    else:
                        intresult = num_input
                    result += str(intresult)
                print(result.rstrip('-87-87'))
            if caesar_decrypt:
                for i in range(len(char_input)):
                    if char_input_list[i].isnumeric():
                        num_input = int(char_input_list[i])
                    else:
                        num_input = char_to_num(char_input_list[i])
                    if 0 <= num_input <= 25:
                        intresult = caesar_unshift(num_input)
                        intresult = num_to_char(intresult)
                    elif num_input == -65:
                        intresult = " "
                    else:
                        intresult = num_input
                    result += str(intresult)
                print(result.rstrip('-87-87'))
window.close()
