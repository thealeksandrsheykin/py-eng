# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию функции get_int_vlan_map из задания 5.
Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта выглядит так:
    interface FastEthernet0/20
    switchport mode access
    duplex auto
То есть, порт находится в VLAN 1.  В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    """
    :param config_filename: имя конфигурационного файла
    :return: возвращает кортеж из двух словарей
    """
    access_dict = dict()
    trunk_dict  = dict()
    with open (config_filename) as file:
        for line in file:
            line = line.rstrip()
            if line.startswith('interface FastEthernet'):
                _,intf = line.split()
                access_dict[intf] = '1'
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access_dict[intf] = vlan
            elif 'allowed vlan' in line:
                vlans = line.split()[-1]
                trunk_dict[intf] = vlans.split(',')
                del access_dict[intf]
            else: continue
    return (access_dict,trunk_dict)

if __name__ == '__main__':
    filename = 'config_sw2.txt'
    print(get_int_vlan_map(filename))