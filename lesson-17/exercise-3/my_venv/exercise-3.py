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

def parse_ch_cdp_neighbors(sh_cdp_neighbors):
    '''
    Функция обрабатывает вывод команды show cdp neighbors
    :param sh_cdp_neighbors: вывод команды одной строкой (не имя файла)
    :return: словарь, который описывает соединения между устройствами
    '''

if __name__ == '__main__':
    with open(r'sh_cdp_n_sw1.txt', 'r') as file:
        parse_sh_cdp_neighbors(file.read())