# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Функция ping_ip_addresses из задания 1 принимает только список адресов, но было бы удобно иметь возможность указывать
адреса с помощью диапазона, например, 192.168.100.1-10.
В этом задании необходимо создать функцию convert_ranges_to_ip_list, которая конвертирует список IP-адресов в разных
форматах в список, где каждый IP-адрес указан отдельно. Функция ожидает как аргумент список IP-адресов и/или диапазонов
IP-адресов.Элементы списка могут быть в формате:
    • 10.1.1.1
    • 10.1.1.1-10.1.1.10
    • 10.1.1.1-10
Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона. Для
упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
Функция возвращает список IP-адресов. Например, если передать функции convert_ranges_to_ip_list такой список:
    ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
Функция должна вернуть такой список:
    ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
    '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
'''

import ipaddress
from pprint import pprint

def convert_ranges_to_ip_list(list_addresses):
    '''
    Функция конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.
    :param ip_addresses: список IP-адресов и/или диапазон IP-адресов
    :return: список IP-адресов
    '''
    result = list()
    for address in list_addresses:
        if '-' in address:
            start_address,end_address = address.split('-')
            ip_1 = ipaddress.ip_address(start_address)
            if end_address.isdigit():
                new_address = '.'.join(start_address.split('.')[:-1]) + '.' + end_address
                ip_2 = ipaddress.ip_address(new_address)
            else:
                ip_2 = ipaddress.ip_address(end_address)
            while ip_1 <= ip_2:
                result.append(str(ip_1))
                ip_1 = ip_1 + 1
        else:
            result.append(address)
    return result

if __name__ == '__main__':
    my_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    pprint(convert_ranges_to_ip_list(my_list))