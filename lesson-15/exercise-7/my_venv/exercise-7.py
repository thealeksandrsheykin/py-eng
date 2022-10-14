# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию get_ints_without_description, которая ожидает как аргумент имя файла, в котором находится конфигурация
устройства. Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов, на которых нет описания (команды
description). Пример интерфейса с описанием:
    interface Ethernet0/2
        description To P_r9 Ethernet0/2
        ip address 10.0.19.1 255.255.255.0
        mpls traffic-eng tunnels
        ip rsvp bandwidth
Интерфейс без описания:
    interface Loopback0
        ip address 10.1.1.1 255.255.255.255
Проверить работу функции на примере файла config_r1.txt
'''
import re

# 1. Cпособ
def get_ints_without_description(filename):
    '''
    Функция должна обрабатывать конфигурацию.
    :param filename: имя файла, в котором находится конфигурация устройства
    :return: возвращать список имен интерфейсов, на которых нет описания (команды description)
    '''
    intf = list()
    regex =r'interface (\S+[\d+/])\n[^!]*'

    with open(filename, 'r') as file:
        for match in re.finditer(regex,file.read()):
            if not re.findall(r'description .*\n',match.group()):
                intf.append(match.group(1))
            else:
                continue
    return intf

# 2. Способ
def get_ints_without_description_2(filename):
    intf = list()
    regex = r'!\ninterface (?P<interface>(\S+))\n(?P<description> description .*)?'

    with open(filename, 'r') as file:
        return [match.group('interface') for match in re.finditer(regex,file.read()) if match.lastgroup == 'interface']

if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))