my_dict = {
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}
str_number = str(input(f'Enter the number: '))
print(f'Number is {str_number}')
len_str_number = len(str_number)

def morse_translator(dict):
    morse_string = ''
    for i in range(len_str_number):
        if str_number[i] in dict:
            symb = dict[str_number[i]]
            morse_string += symb
    return morse_string

print(f'Morse line: {morse_translator(my_dict)}')