import json

class Morse():
    def morse_translator(self, orig_str, morse_dict):
        len_str_number = len(orig_str)
        morse_string = ''
        for i in range(len_str_number):

            if orig_str[i].islower() == True:
                symb_buffer = orig_str[i].upper()
            else:
                symb_buffer = orig_str[i]

            if symb_buffer in morse_dict:
                symb = morse_dict[symb_buffer]
                morse_string += symb
        return morse_string

with open('dict.json', 'r', encoding='utf-8') as dt:
    my_dict = json.load(dt)

orig_line = str(input(f'Enter the line: '))
translate = Morse().morse_translator(orig_line, my_dict)

print(f'Original line: {orig_line}')
print(f'Morse line: {translate}')