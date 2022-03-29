# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию скрипта задания 2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
    • состоит из 4 чисел (а не букв или других символов)
    • числа разделенны точкой
    • каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес». Сообщение «Неправильный IP-адрес» должно
выводиться только один раз, даже если несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-aдрес в формате A.B.C.D: ')
flag = True

my_list = ip.split('.')

if len(my_list) != 4:
    flag = False
else:
    for i in my_list:
        if not (i.isdigit() and int(i) in range(256)):
            flag = False
        else:
            pass


if not flag:
    print(f'Неправильный IP-адрес')
else:
    if 1 <= int(my_list[0]) <= 223:
        print (f'unicast')
    elif 224 <= int(my_list[0]) <= 239:
        print(f'multicast')
    elif ip == '255.255.255.255':
        print(f'local broadcast')
    elif ip == '0.0.0.0':
        print(f'unassigned')
    else:
        print(f'unused')
