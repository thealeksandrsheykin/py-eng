# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
data = argv[1]
tag = False

with open(data, 'r+') as src_file, open('config_sw1_cleared.txt', 'w') as dst_file:
      for i in src_file:
            if i.startswith('!'): continue
            for j in ignore:
                  if j in i:
                        tag = True
                        break
                  else: pass
            if not tag:
                 dst_file.write(i.strip(' '))
            else: tag = False
