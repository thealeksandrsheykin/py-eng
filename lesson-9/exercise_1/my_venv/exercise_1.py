# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию, которая генерирует конфигурацию для access-портов. Функция ожидает такие аргументы:
    1. словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    2. шаблон конфигурации access-портов в виде списка команд (список access_mode_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template. В
конце строк в списке не должно быть символа перевода строки. В этом задании заготовка для функции уже сделана и надо
только продолжить писать само тело функции.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
    "interface FastEthernet0/12",
    "switchport mode access",
    "switchport access vlan 10",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
    "interface FastEthernet0/17",
    "switchport mode access",
    "switchport access vlan 150",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
...]

Проверить работу функции на примере словаря access_config и списка команд access_mode_template. Если предыдущая проверка
прошла успешно, проверить работу функции еще раз на словаре access_config_2 и убедиться, что в итоговом списке правильные
номера интерфейсов и вланов.
Ограничение: Все задания надо выполнять используя только пройденные темы.

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
    ]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
    }

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
    }
"""

def generate_access_config(intf_vlan_mapping,access_template):
    """
    :param intf_valn_mapping: словарь с соответствием интерфейс-VLAN такого вида:
                                        {"FastEthernet0/12": 10,
                                         "FastEthernet0/14": 11,
                                         "FastEthernet0/16": 17}
    :param access_template:  список команд для порта в режиме access
    :return: список всех портов в режиме access с конфигурацией на основе шаблона
    """
    my_list = list()
    for intf,vlan in intf_vlan_mapping.items():
        my_list.append(f'interface {intf}')
        for line in access_template:
            if line.endswith('vlan'):
                my_list.append(f'{line} {vlan}')
            else:
                my_list.append(f'{line}')
    return my_list

if __name__ == '__main__':

    access_mode_template = [
        "switchport mode access", "switchport access vlan",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

    access_config = {
        "FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17
    }

    access_config_2 = {
        "FastEthernet0/03": 100,
        "FastEthernet0/07": 101,
        "FastEthernet0/09": 107,
    }

    for i in generate_access_config(access_config_2,access_mode_template):
        print(i)


