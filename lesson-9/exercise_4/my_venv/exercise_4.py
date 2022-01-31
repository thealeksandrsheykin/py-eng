# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию функции generate_trunk_config из задания 3 Изменить функцию таким образом, чтобы она возвращала не список
команд, а словарь:
    • ключи: имена интерфейсов, вида «FastEthernet0/1»
    • значения: список команд, который надо выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    :param   intf_vlan_mapping: словарь с соответствием интерфейс-VLANы
    :param   trunk_template: шаблон конфигурации trunk-портов в виде списка команд
    :return: словарь:
                • ключи: имена интерфейсов, вида «FastEthernet0/1»
                • значения: список команд, который надо выполнить на этом интерфейсе
    """

    my_dict = dict()
    for intf,vlans in trunk_config.items():
        my_list = list()
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                my_list.append(f'{line} {",".join([str(j) for j in vlans])}')
            else:
                my_list.append(line)
        my_dict[intf] = my_list
    return my_dict



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
    print(generate_trunk_config(trunk_config,trunk_mode_template))
