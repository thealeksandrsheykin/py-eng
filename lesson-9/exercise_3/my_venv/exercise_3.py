# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов. У функции должны быть такие
параметры:
    1. intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
        {"FastEthernet0/1": [10, 20],
         "FastEthernet0/2": [11, 30],
         "FastEthernet0/4": [17]}
    2. trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд
    (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_mode_template. В конце
строк в списке не должно быть символа перевода строки. Проверить работу функции на примере словаря trunk_config и списка
команд trunk_mode_template. Если эта проверка прошла успешно, проверить работу функции еще раз на словаре trunk_config_2
и убедится, что в итоговом списке правильные номера интерфейсов и вланов.
Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

[
"interface FastEthernet0/1",
"switchport mode trunk",
"switchport trunk native vlan 999",
"switchport trunk allowed vlan 10,20,30",
"interface FastEthernet0/2",
"switchport mode trunk",
"switchport trunk native vlan 999",
"switchport trunk allowed vlan 11,30",
...]

Ограничение: Все задания надо выполнять используя только пройденные тем

trunk_mode_template = [
"switchport mode trunk", "switchport trunk native vlan 999",
"switchport trunk allowed vlan"
]
trunk_config = {
"FastEthernet0/1": [10, 20, 30],
"FastEthernet0/2": [11, 30],
"FastEthernet0/4": [17]
}

"""

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    :param   intf_vlan_mapping: словарь с соответствием интерфейс-VLANы
    :param   trunk_template: шаблон конфигурации trunk-портов в виде списка команд
    :return: список команд с конфигурацией
    """
    my_list = list()
    for intf,vlans in trunk_config.items():
        my_list.append(f'interface {intf}')
        for line in trunk_template:
            if line.endswith('allowed vlan'):

                my_list.append(f'{line} {",".join([str(j) for j in vlans])}')
            else:
                my_list.append(line)
    return my_list



if __name__ == '__main__':

    trunk_mode_template = [
        "switchport mode trunk", "switchport trunk native vlan 999",
        "switchport trunk allowed vlan"
    ]

    trunk_config = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17]
    }
    for i in generate_trunk_config(trunk_config,trunk_mode_template):
        print(f'{i}')

