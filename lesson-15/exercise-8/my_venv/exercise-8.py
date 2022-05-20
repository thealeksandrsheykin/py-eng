# -*- coding: utf-8 -*-
# !/usr/bin/env pyton3

'''
Создать функцию generate_description_from_cdp, которая ожидает как аргумент имя файла, в котором находится вывод команды
show cdp neighbors. Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды
описание для интерфейсов. Например, если у R1 такой вывод команды:
R1>show cdp neighbors
    Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                      S - Switch, H - Host, I - IGMP, r - Repeater
Device ID Local Intrfce Holdtme Capability Platform   Port ID
SW1       Eth 0/0       140         S I     WS-C3750- Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание description Connected to SW1 port Eth 0/1.
Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
    "Eth 0/0": "description Connected to SW1 port Eth 0/1"
Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''
import re

def generate_description_from_cdp(filename):
    '''
    Функция обрабатывает вывод команды show cdp neighbors
    :param filename: имя файла, в котором находится вывод команды show cdp neighbors
    :return: словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса
    '''
    des_con_lcl_int = dict() #description connect local interface
    template = 'description Connected to {} port {}'
    regex = r'(?P<rdev>\S+) +(?P<lport>\S+ \S+) +\d+ +[\w ]+  +\S+ +(?P<rport>\S+ \S+)'

    with open(filename, 'r') as file:
        for match in re.finditer(regex,file.read()):
            des_con_lcl_int[match.group('lport')] = template.format(*match.group('rdev','rport'))
    return des_con_lcl_int


if __name__ == '__main__':
    for i,j in generate_description_from_cdp('sh_cdp_n_sw1.txt').items():
        print(f'Интерфейс: {i} Описание: {j}')
