# -*- coding: utf-8 -*-
# /!usr/bin/env python3

"""
Cоздайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться при необходимости добавить VLAN на
коммутатор. В шаблоне должны поддерживаться возможности:
    • добавления VLAN и имени VLAN
    • добавления VLAN как access, на указанном интерфейсе
    • добавления VLAN в список разрешенных, на указанные транки
Если VLAN необходимо добавить как access, надо настроить и режим интерфейса и добавить его в VLAN:
    interface Gi0/1
        switchport mode access
        switchport access vlan 5
Для транков, необходимо только добавить VLAN в список разрешенных:
    interface Gi0/10
        switchport trunk allowed vlan add 5

Имена переменных надо выбрать на основании примера данных, в файле data_files/add_vlan_to_switch.yaml. Проверьте шаблон
templates/add_vlan_to_switch.txt на данных в файле data_files/add_vlan_to_switch.yaml, с помощью функции generate_config
из задания 1. Не копируйте код функции generate_config.
"""

import yaml
from exercise01 import generate_config


if __name__ == '__main__':
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
