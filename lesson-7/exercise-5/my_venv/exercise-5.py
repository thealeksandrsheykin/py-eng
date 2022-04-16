# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
src,dst = argv[1:]
tag = False

with open(src, 'r+') as src_file, open(dst, 'w') as dst_file:
      for i in src_file:
            for j in ignore:
                  if j in i:
                        tag = True
                        break
                  else: pass
            if not tag:
                 dst_file.write(i.strip(' '))
            else: tag = False
