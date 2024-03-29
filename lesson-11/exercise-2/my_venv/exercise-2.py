# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Создать функцию create_network_map, которая обрабатывает вывод команды show cdp neighbors из нескольких файлов и объеди-
няет его в одну общую топологию. У функции должен быть один параметр filenames, который ожидает как аргумент список с
именами файлов, в которых находится вывод команды show cdp neighbors. Функция должна возвращать словарь, который описы -
вает соединения между устройствами. Структура словаря такая же, как в задании 1:

{("R4", "Fa0/1"): ("R5", "Fa0/1"),
 ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Cгенерировать топологию, которая соответствует выводу из файлов:
    • sh_cdp_n_sw1.txt
    • sh_cdp_n_r1.txt
    • sh_cdp_n_r2.txt
    • sh_cdp_n_r3.txt
Не копировать код функций parse_cdp_neighbors и draw_topology. Если функция parse_cdp_neighbors не может обработать вывод
одного из файлов с выводом команды, надо исправить код функции в задании 1.
Ограничение: Все задания надо выполнять используя только пройденные темы.

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt"]

'''

from exercise import parse_cdp_neighbors


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
           my_dict |= parse_cdp_neighbors(file.read()) # python 3.9
           # my_dict.update(parse_cdp_neighbors(file.read()))
    return my_dict



if __name__ == '__main__':
    infiles = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt"]
    for i,j in create_network_map(infiles).items():
        print(f' Device {i[0]}({i[1]}) --> Device {j[0]}({j[1]})')
