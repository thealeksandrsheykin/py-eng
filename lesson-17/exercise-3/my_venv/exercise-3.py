# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию parse_sh_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors. Функция ожидает, как
аргумент, вывод команды одной строкой (не имя файла). Функция должна возвращать словарь, который описывает соединения
между устройствами. Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors
    Device ID   Local Intrfce   Holdtme Capability  Platform    Port ID
      R5           Fa 0/1         122      R S I      2811       Fa 0/1
      R6           Fa 0/2         143      R S I      2811       Fa 0/0
Функция должна вернуть такой словарь:
    {"R4": {"Fa 0/1": {"R5": "Fa 0/1"}, "Fa 0/2": {"R6": "Fa 0/0"}}}
Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

import re

def parse_sh_cdp_neighbors(sh_cdp_neighbors):
    '''
    Функция обрабатывает вывод команды show cdp neighbors
    :param sh_cdp_neighbors: вывод команды одной строкой (не имя файла)
    :return: словарь, который описывает соединения между устройствами
    '''
    neighbor_dict = {}

    regex = (
        '(?P<dev>\S+)>.*'
        '|(?P<neighbor>\S+) +(?P<lintf>\S+ [\d+/]+).*?(?P<rintf>\S+ [\d+/]+).*')

    for match in re.finditer(regex,sh_cdp_neighbors):
        if match.lastgroup == 'dev':
            device = match.group(match.lastgroup)
            neighbor_dict[device] = {}
        else:
            neighbor, lintf, rintf = match.group('neighbor', 'lintf', 'rintf')
            neighbor_dict[device][lintf] = {neighbor: rintf}
    return neighbor_dict

if __name__ == '__main__':
    with open(r'sh_cdp_n_sw1.txt', 'r') as file:
        for key,value in parse_sh_cdp_neighbors(file.read()).items():
            print(f'Device: {key}')
            for i,j in value.items():
                print(f'\tLocal Interface: {i} -> Device: {list(j.keys())[0]} Interface: {list(j.values())[0]} ')