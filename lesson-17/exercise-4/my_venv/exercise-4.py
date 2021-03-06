# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и
записывает итоговую топологию в один словарь. Функция generate_topology_from_cdp должна быть создана с параметрами:
    • list_of_files    - список файлов из которых надо считать вывод команды sh cdp neighbor
    • save_to_filename - имя файла в формате YAML, в который сохранится топология.
        – значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
        – топология сохраняется только, если save_to_filename как аргумент указано имя файла
Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли
топология в файл. Структура словаря должна быть такой:
    {"R4": {"Fa 0/1": {"R5": "Fa 0/1"},
            "Fa 0/2": {"R6": "Fa 0/0"}},
    "R5":  {"Fa 0/1": {"R4": "Fa 0/1"}},
    "R6":  {"Fa 0/0": {"R4": "Fa 0/2"}}}
Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
Проверить работу функции generate_topology_from_cdp на списке файлов:
    • sh_cdp_n_sw1.txt
    • sh_cdp_n_r1.txt
    • sh_cdp_n_r2.txt
    • sh_cdp_n_r3.txt
    • sh_cdp_n_r4.txt
    • sh_cdp_n_r5.txt
    • sh_cdp_n_r6.txt
Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.
'''
import re
import yaml
from glob import glob
from datetime import datetime

def generate_topology_from_cdp(list_of_files,save_to_filename=None):
    '''
    Функция обрабатывает вывод команды show cdp neighbor из нескольких файлов
    :param list_of_files: список файлов из которых надо считать вывод команды sh cdp neighbor
    :param save_to_filename: имя файла в формате YAML, в который сохранится топология.
    :return: словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл
    '''
    neighbor_dict = {}
    regex = (r'(?P<neighbor>\S+) +(?P<lintf>\S+ [\d+/]+).*?(?P<rintf>\S+ [\d+/]+)')

    for file in list_of_files:
        hostname = re.search(r'.*_(\S+).txt',file).group(1).upper()
        neighbor_dict[hostname] = {}
        with open(file, 'r') as file_in:
            for match in re.finditer(regex, file_in.read()):
                neighbor,lintf,rintf = match.group('neighbor', 'lintf', 'rintf')
                neighbor_dict[hostname][lintf] = {neighbor: rintf}
    if save_to_filename:
        with open(save_to_filename, 'w+') as file_out:
            yaml.dump(neighbor_dict,file_out,default_flow_style=False)
    return neighbor_dict


if __name__ == '__main__':
    list_of_files =glob('sh_cdp_n_*.txt')
    data = generate_topology_from_cdp(list_of_files,'{:res_%H_%M_%S.yml}'.format(datetime.now()))
    for key, value in data.items():
        print(f'Device: {key}')
        for i, j in value.items():
            print(f'\tLocal Interface: {i} -> Device: {list(j.keys())[0]} Interface: {list(j.values())[0]} ')
