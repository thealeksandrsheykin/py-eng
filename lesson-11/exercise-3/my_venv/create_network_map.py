# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import parse_cdp_neighbors as pcn

def create_network_map(filenames):
    """
    Функция обрабатывает вывод команды show cdp neighbors из нескольких файлов и объединяет
    его в одну общую топологию.
    :param filenames: список с именами файлов, в которых находится вывод команды show cdp neighbors
    :return: словарь, который описывает соединения между устройствами
    """
    my_dict = dict()
    for filename in filenames:
        with open(filename) as file:
           my_dict |= pcn.parse_cdp_neighbors(file.read()) # python 3.9
           # my_dict.update(parse_cdp_neighbors(file.read()))
    return my_dict



if __name__ == '__main__':
    infiles = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt"]
    for i,j in create_network_map(infiles).items():
        print(f' Device {i[0]}({i[1]}) --> Device {j[0]}({j[1]})')
