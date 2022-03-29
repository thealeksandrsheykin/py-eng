# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию скрипта задания 5. Переделать скрипт: Отсортировать вывод по номеру VLAN В результате должен получиться
такой вывод:
    10   01ab.c5d0.70d0 Gi0/8
    10   0a1b.1c80.7000 Gi0/4
    100  01bb.c580.7000 Gi0/1
    200  0a4b.c380.7c00 Gi0/2
    200  1a4b.c580.7000 Gi0/6
    300  0a1b.5c80.70f0 Gi0/7
    300  a2ab.c5a0.700e Gi0/3
    500  02b1.3c80.7b00 Gi0/5
    1000 0a4b.c380.7d00 Gi0/9
Обратите внимание на vlan 1000 - он должен выводиться последним. Правильной сортировки можно добиться, если vlan будет
числом, а не строкой.
"""
# Первый вариант
my_list = list()
with open (r'CAM_table.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        if '.' in line:
            line = line.replace('DYNAMIC','')
            line_list = line.split()
            line_list[0] = int(line_list[0])
            my_list.append(line_list)
        else:
            continue

for line in sorted(my_list):
    print(f'{line[0]:<5} {line[1]:<15} {line[2]:<5}')



