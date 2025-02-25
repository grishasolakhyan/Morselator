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
morse_string = ''
for i in range(len_str_number):
    if str_number[i] in my_dict:
        symb = my_dict[str_number[i]]
        morse_string+=symb
print(f'Morse line: {morse_string}')