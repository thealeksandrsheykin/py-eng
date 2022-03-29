# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию скрипта задания 6.
Переделать скрипт:
    • Запросить у пользователя ввод номера VLAN.
    • Выводить информацию только по указанному VLAN.
Пример работы скрипта:
    Enter VLAN number: 10
    10 0a1b.1c80.7000 Gi0/4
    10 01ab.c5d0.70d0 Gi0/8
Ограничение: Все задания надо выполнять используя только пройденные темы
"""
vlan = input('Enter VLAN number: ')

with open (r'CAM_table.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        line_list = line.split()
        if line_list and line_list[0].isdigit and line_list[0] == vlan:
            print(f'{line_list[0]:<5} {line_list[1]:<15} {line_list[3]:<5}')
        else:
            continue


