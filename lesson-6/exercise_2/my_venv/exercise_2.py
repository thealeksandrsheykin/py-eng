# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
    • «unicast» - если первый байт в диапазоне 1-223
    • «multicast» - если первый байт в диапазоне 224-239
    • «local broadcast» - если IP-адрес равен 255.255.255.255
    • «unassigned» - если IP-адрес равен 0.0.0.0
    • «unused» - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = input('Введите IP-aдрес в формате A.B.C.D: ')

my_list = ip.split('.')
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