# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент имя файла, в котором находится вывод команды show ip int br
Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
    • Interface
    • IP-Address
    • Status
    • Protocol
Информация должна возвращаться в виде списка кортежей:
    [("FastEthernet0/0", "10.0.1.1", "up", "up"), ("FastEthernet0/1", "10.0.2.1", "up", "up"), ("FastEthernet0/2", "unassigned", "down", "down")]
Для получения такого результата, используйте регулярные выражения. Проверить работу функции на примере файла sh_ip_int_br.txt.
'''
import re


def parse_sh_ip_int_br(filename):
    '''
    Функция обрабатывает вывод команды show ip int br
    :param filename: имя файла, в котором находится вывод команды show ip int br
    :return: список кортежей с полями (Interface, IP-address, Status, Protocol)
    '''

    regex = r'(\S+) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'
    with open (filename) as file:
        return [i for i in re.findall(regex, file.read())]

if __name__ == '__main__':
    for intf in parse_sh_ip_int_br('sh_ip_int_br.txt'):
        print(intf)

