# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию скрипта задания 3.
Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    flag = True
    ip = input('Введите IP-aдрес в формате A.B.C.D: ')
    my_list = ip.split('.')

    if len(my_list) != 4:
        print(f'IP-адрес введен неверно. Попробуйте еще раз...')
        flag = False
        continue
    else:
        for i in my_list:
            if not (i.isdigit() and int(i) in range(256)):
                print(f'IP-адрес неправильный. Введите еще раз...')
                flag = False
                break
    if flag:
        break

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