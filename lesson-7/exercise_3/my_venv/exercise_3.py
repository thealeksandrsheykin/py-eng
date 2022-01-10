# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Сделать копию скрипта задания 2.
Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
При этом скрипт также не должен выводить строки, которые начинаются на !.
Проверить работу скрипта на конфигурационном файле config_sw1.txt. Имя файла передается как аргумент скрипту.
Ограничение: Все задания надо выполнять используя только пройденные темы.
ignore = ["duplex", "alias", "configuration"]
"""
ignore = ["duplex", "alias", "configuration"]

# Первый вариант
with open (r'config_sw1.txt', 'r') as file:
    for line in file:
        flag = False
        for word in ignore:
            if word in line:
                flag = True
                break
        if line.startswith('!') or flag:
            continue
        else:
            print(f'{line.rstrip()}')