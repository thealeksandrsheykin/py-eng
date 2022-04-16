# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
data = argv[1]
tag = False

with open(data, 'r+') as file:
      for i in file:
            if i.startswith('!'): continue
            for j in ignore:
                  if j in i:
                        tag = True
                        break
                  else: pass
            if not tag:
                  print(i.strip(' \n'))
            else: tag = False
                        
                  
            
            
            

