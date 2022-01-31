# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух
словарей:
    1. словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    2. словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    """
    :param config_filename: имя конфигурационного файла
    :return: возвращает кортеж из двух словарей
    """
    access_dict = dict()
    trunk_dict = dict()
    with open (config_filename) as file:
        for line in file:
            line = line.rstrip()
            if line.startswith('interface '):
                _,intf = line.split()
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access_dict[intf] = vlan
            elif 'allowed vlan' in line:
                vlans = line.split()[-1]
                trunk_dict[intf] =vlans.split(',')
            else: continue
    return (access_dict,trunk_dict)

if __name__ == '__main__':
    filename = 'config_sw1.txt'
    print(get_int_vlan_map(filename))