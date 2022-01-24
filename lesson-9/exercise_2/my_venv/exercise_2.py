# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию функции generate_access_config из задания 1.
Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли настроен port-security:
    • имя параметра «psecurity»
    • по умолчанию значение None
    • для настройки port-security, как значение надо передать список команд port-security (находятся в списке
      port_security_template)
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template и
шаблона port_security_template, если он был передан. В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря access_config, с генерацией конфигурации port-security и без.
Пример вызова функции:
    print(generate_access_config(access_config, access_mode_template))
    print(generate_access_config(access_config, access_mode_template, port_security_template))
Ограничение: Все задания надо выполнять используя только пройденные темы
    access_mode_template = [
        "switchport mode access", "switchport access vlan",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

    port_security_template = [
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security"
    ]

    access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
"""

def generate_access_config(intf_vlan_mapping,access_template,psecurity=None):
    """
    :param intf_valn_mapping: словарь с соответствием интерфейс-VLAN такого вида:
                                        {"FastEthernet0/12": 10,
                                         "FastEthernet0/14": 11,
                                         "FastEthernet0/16": 17}
    :param access_template:  список команд для порта в режиме access
    :param psecurity: список команд port-security
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
        if psecurity:
            for line in psecurity:
                my_list.append(f'{line}')
    return my_list

if __name__ == '__main__':
    access_mode_template = [
        "switchport mode access", "switchport access vlan",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

    port_security_template = [
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security"
    ]

    access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

    for i in generate_access_config(access_config, access_mode_template, port_security_template):
        print(i)
