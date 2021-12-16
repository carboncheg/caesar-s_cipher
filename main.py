from time import sleep

print('Добро пожаловать в приложение "Шифр Цезаря"')
sleep(1.5)

cipher = '0'
alphabet = '0'
step = '0'

while True:
    cipher = input('Что вы хотите сделать? (1 - зашифровать, 2 - расшифровать) ')
    if cipher == '1' or cipher == '2':
        break
    else:
        print('Введите число "1" для шифрования или число "2" для дешифрования')
        continue

while True:
    alphabet = input('Выберите алфавит: (1 - английский, 2 - русский) ')
    if alphabet == '1' or alphabet == '2':
        break
    else:
        print('Введите число "1" для выбора английского алфавита или число "2" - для русского')
        continue

if alphabet == '1':
    while True:
        step = input('Укажите шаг сдвига (от 1 до 25): ')
        if step.isdigit() and 0 < int(step) <= 25:
            break
        else:
            print('Введите целое положительное число')
            continue

if alphabet == '2':
    while True:
        step = input('Укажите шаг сдвига (от 1 до 31): ')
        if step.isdigit() and 0 < int(step) <= 31:
            break
        else:
            print('Введите целое положительное число')
            continue

input_txt_en = 'Введите текст на английском языке:\n'
input_sym_en = 'Введите символы английского алфавита:\n'
input_txt_ru = 'Введите текст на русском языке:\n'
input_sym_ru = 'Введите символы русского алфавита:\n'
ord_f_en = ord('a')
ord_l_en = ord('z')
ord_f_ru = ord('а')
ord_l_ru = ord('я')

def check_validity(input_txt, input_sym, ord_f, ord_l):
    flag = False
    while not flag:
        if cipher == '1':
            symbol_set = input(input_txt)
        elif cipher == '2':
            symbol_set = input(input_sym)
        if symbol_set == '':
            continue
        lower_symbol_set = symbol_set.lower()
        for i in range(ord_f, ord_l + 1):
            if chr(i) not in lower_symbol_set:
                continue
            else:
                flag = True
                break
    return symbol_set

if alphabet == '1':
    symbol_set = check_validity(input_txt_en, input_sym_en, ord_f_en, ord_l_en)

elif alphabet == '2':
    symbol_set = check_validity(input_txt_ru, input_sym_ru, ord_f_ru, ord_l_ru)

def encrypt():
    lower_symbol_set = symbol_set.lower()
    for i in range(len(lower_symbol_set)):
        sym_num = ord(lower_symbol_set[i])
        if start_alphabet < sym_num <= end_alphabet:
            encrypt_sym_num = sym_num + int(step)
            if encrypt_sym_num > end_alphabet:
                remainder = encrypt_sym_num - end_alphabet
                encrypt_sym_num = start_alphabet + remainder
            if symbol_set[i].isupper():
                print((chr(encrypt_sym_num)).upper(), end='')
            else:
                print(chr(encrypt_sym_num), end='')
        else:
            print(symbol_set[i], end='')

def decrypt():
    lower_symbol_set = symbol_set.lower()
    for i in range(len(lower_symbol_set)):
        sym_num = ord(lower_symbol_set[i])
        if start_alphabet <= sym_num < end_alphabet:
            decrypt_sym_num = sym_num - int(step)
            if decrypt_sym_num < start_alphabet:
                remainder = start_alphabet - decrypt_sym_num
                decrypt_sym_num = end_alphabet - remainder
            if symbol_set[i].isupper():
                print((chr(decrypt_sym_num)).upper(), end='')
            else:
                print(chr(decrypt_sym_num), end='')
        else:
            print(symbol_set[i], end='')

if cipher == '1' and alphabet == '1':
    start_alphabet = ord('a') - 1
    end_alphabet = ord('z')
    encrypt()
elif cipher == '1' and alphabet == '2':
    start_alphabet = ord('а') - 1
    end_alphabet = ord('я')
    encrypt()
if cipher == '2' and alphabet == '1':
    start_alphabet = ord('a')
    end_alphabet = ord('z') + 1
    decrypt()
elif cipher == '2' and alphabet == '2':
    start_alphabet = ord('а')
    end_alphabet = ord('я') + 1
    decrypt()
