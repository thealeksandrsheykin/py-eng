# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Проверить работу функции get_ip_from_cfg из задания 2 на конфигурации config_r2.txt.
Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
    interface Ethernet0/1
        ip address 10.255.2.2 255.255.255.0
        ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1 соответствует только один из них (второй).
Скопировать функцию get_ip_from_cfg из задания 2 и переделать ее таким образом, чтобы она возвращала список кортежей
для каждого интерфейса. Если на интерфейсе назначен только один адрес, в списке будет один кортеж. Если же на интерфейсе
настроены несколько IP-адресов, то в списке будет несколько кортежей. Проверьте функцию на конфигурации config_r2.txt и
убедитесь, что интерфейсу Ethernet0/1 соответствует список из двух кортежей.
Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса, диапазоны адресов и так далее, так как
обрабатывается вывод команды, а не ввод пользователя.
'''
import re

def get_ip_from_cfg(filename):
    '''
    Функция обрабатывает конфигурацию
    :param filename: имя файла
    :return: возвращает словарь:
                • ключ:     имя интерфейса
                • значение: кортеж с двумя строками:
                            – IP-адрес
                            – Маска
    '''
    intf_dict = dict()
    regex =(r'interface (\S+)\n(?: .*\n)* ip address \S+ \S+\n( ip address \S+ \S+ secondary\n)*')

    with open(filename, 'r') as file:
        for match in re.finditer(regex, file.read()):
            intf_dict[match.group(1)] = re.findall(r'ip address (\S+) (\S+)', match.group())
    return intf_dict


if __name__ == '__main__':
    for intf,addresses in get_ip_from_cfg('config_r2.txt').items():
        print(f'На интерфейсе {intf} настроены адреса: {addresses}')

