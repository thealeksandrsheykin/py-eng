# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt, которые генерируют конфигурацию IPsec over
GRE между двумя маршрутизаторами. Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля, а
templates/gre_ipsec_vpn_2.txt - для второй.
Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах: cisco_vpn_1.txt и cisco_vpn_2.txt.
Создать функцию create_vpn_config, которая использует эти шаблоны для генерации конфигурации VPN на основе данных в
словаре data.
Параметры функции:
    • template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
    • template2 - имя файла с шаблоном, который создает конфигурацию для второй стронытуннеля
    • data_dict - словарь со значениями, которые надо подставить в шаблоны
Функция должна возвращать кортеж с двумя конфигурациямя (строки), которые получены на основе шаблонов.
Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах cisco_vpn_1.txt и cisco_vpn_2.txt
data = {
    'tun_num': 10,
    'wan_ip_1': '192.168.100.1',
    'wan_ip_2': '192.168.100.2',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
}
"""
from exercise01 import generate_config


def create_vpn_config(template01: str, template02: str, data_dict: dict) -> tuple:
    """
    The function generates a VPN configuration based on a dictionary and templates
    :param template02:
    :param template01:
    :param template1: filename template for first side
    :param template2: filename template for second side
    :param data_dict: dictionary with values to replace in the template
    :return: tuple with two configuration (string)
    """
    return generate_config(template01, data_dict), generate_config(template02, data_dict)


if __name__ == '__main__':
    template_file01 = 'templates/gre_ipsec_vpn_1.txt'
    template_file02 = 'templates/gre_ipsec_vpn_2.txt'
    data = {
        'tun_num': 10,
        'wan_ip_1': '192.168.100.1',
        'wan_ip_2': '192.168.100.2',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    result_vpn01, result_vpn02 = create_vpn_config(template_file01, template_file02, data)
    print(f'{result_vpn01}\n'
          f'#--------------#\n'
          f'{result_vpn02}\n')
