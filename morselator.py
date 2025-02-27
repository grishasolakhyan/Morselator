import json

with open('dict.json', 'r', encoding='utf-8') as dt:
    my_dict = json.load(dt)

orig_line = str(input(f'Enter the line: '))
print(f'Original line: {orig_line}')

def morse_translator(orig_str, dict):
    len_str_number = len(orig_str)
    morse_string = ''
    for i in range(len_str_number):

        print(f'{orig_str[i]} -> {orig_str[i].isupper()}')
        if orig_str[i].islower() == True:
            symb_buffer = orig_str[i].upper()
        else:
            symb_buffer = orig_str[i]

        if symb_buffer in dict:
            symb = dict[symb_buffer]
            morse_string += symb
    return morse_string

print(f'Morse line: {morse_translator(orig_line, my_dict)}')