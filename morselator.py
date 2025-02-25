import json

with open('dict.json', 'r', encoding='utf-8') as dt:
    my_dict = json.load(dt)

orig_line = str(input(f'Enter the line: '))
print(f'Original line: {orig_line}')

def morse_translator(orig_str, dict):
    len_str_number = len(orig_str)
    morse_string = ''
    for i in range(len_str_number):
        if orig_str[i] in dict:
            symb = dict[orig_str[i]]
            morse_string += symb
    return morse_string

print(f'Morse line: {morse_translator(orig_line, my_dict)}')