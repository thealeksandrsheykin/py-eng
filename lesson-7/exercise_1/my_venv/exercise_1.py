# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде
на стандартный поток вывода:
Prefix 10.0.24.0/24
AD/Metric 110/41
Next-Hop 10.0.13.3
Last update 3d18h
Outbound Interface FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
array = list()
with open (r'ospf.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        line = line.replace('[','').replace(']','')
        line = line.replace('via','').replace(',','')
        array = line.split()[1:]
        print(f'Prefix {array[0]}\n'
              f'AD/Metric {array[1]}\n'
              f'Next-Hop {array[2]}\n'
              f'Last update {array[3]}\n'
              f'Outbound Interface {array[4]}\n')

