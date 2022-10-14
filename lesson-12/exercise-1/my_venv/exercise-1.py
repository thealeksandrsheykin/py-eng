# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Функция ожидает как аргумент список IP-адресов.
Функция должна возвращать кортеж с двумя списками:
    • список доступных IP-адресов
    • список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def ping_ip_addresses(list_addresses):
    '''
    Функция проверяет пингуются ли IP-адреса.
    :param list_addresses: список IP-адресов.
    :return: кортеж с двумя списками (список доступных IP-адресов, список недоступных IP-адресов)
    '''
    reach = list()
    unreach = list()
    for ip_address in list_addresses:
        icmp = subprocess.run(['ping','-n','1',ip_address], stdout=subprocess.DEVNULL)
        if not icmp.returncode:
            reach.append(ip_address)
        else:
            unreach.append(ip_address)
    return (reach,unreach)


if __name__ == '__main__':
    my_list = ['192.168.73.40','192.168.73.4','192.168.73.5','192.168.73.48']
    result = ping_ip_addresses(my_list)
    print(f'Доступные адреса: {result[0]}\n'
          f'Недоступные адреса: {result[1]}')