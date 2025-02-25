my_dict = {
    'A':	'.-',
    'B':	'-...',
    'C':	'-.-.',
    'D':	'-..',
    'E':	'.',
    'F':	'..-.',
    'G':	'--.',
    'H':	'....',
    'I':	'..',
    'J':	'.---',
    'K':	'-.-',
    'L':	'.-..',
    'M':	'--',
    'N':	'-.',
    'O':	'---',
    'P':	'.--.',
    'Q':	'--.-',
    'R':	'.-.',
    'S':	'...',
    'T':	'-',
    'U':	'..-',
    'V':	'...-',
    'W':	'.--',
    'X':	'-..-',
    'Y':	'-.--',
    'Z':	'--..',
    '0':	'-----',
    '1':	'.----',
    '2':	'..---',
    '3':	'...--',
    '4':	'....-',
    '5':	'.....',
    '6':	'-....',
    '7':	'--...',
    '8':	'---..',
    '9':	'----.',
    ' ': ' '
}
orig_line = str(input(f'Enter the number: '))
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