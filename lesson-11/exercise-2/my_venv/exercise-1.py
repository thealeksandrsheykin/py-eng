# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.
У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя фай-
ла). Для этого надо считать все содержимое файла в строку, а затем передать строку как аргумент функции (как передать вы-
вод команды показано в коде ниже). Функция должна возвращать словарь, который описывает соединения между устройствами.
Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors
    Device ID Local Intrfce Holdtme Capability Platform Port ID
        R5      Fa 0/1        122     R S I      2811     Fa 0/1
        R6      Fa 0/2        143     R S I      2811     Fa 0/0

Функция должна вернуть такой словарь:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
    ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0. Проверить
работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция работать и на других файлах (тест проверяет работу
функции на выводе из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command_output):
    my_dict = dict()
    for line in command_output.split('\n'):
        if '>' in line:
            local_dev = line.split('>')[0]
            continue
        else:
            my_list = line.split()
            if len(my_list) > 5 and my_list[3].isdigit():
                remote_dev, local_type, local_num, *other, remote_type, remote_num = my_list
                my_dict[(local_dev, local_type + local_num)] = (remote_dev,remote_type+remote_num)
    return my_dict

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
