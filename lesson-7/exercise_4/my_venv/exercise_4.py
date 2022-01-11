# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Переделать скрипт из задания 3: вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в
файл.
Имена файлов нужно передавать как аргументы скрипту:
    • имя исходного файла конфигурации
    • имя итогового файла конфигурации
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore и строки, которые начинаются на „!“.
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys

file_read,file_write = sys.argv[1:]

ignore = ["duplex", "alias", "configuration"]

with open(file_read, 'r') as f_read, open(file_write, 'w') as f_write:
    for line in f_read:
        line_array = line.split()
        line_set = set(line_array) & set(ignore)
        if line.startswith('!') or line_set:
            continue
        else:
            f_write.write(f'{line.rstrip()}\n')
