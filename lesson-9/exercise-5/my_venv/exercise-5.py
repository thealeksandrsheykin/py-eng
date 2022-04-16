# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
      '''
      -config_filename ожидает как аргумент имя конфигурационного файла.
      Функция возвращает кортеж из двух словарей:
            -словарь портов в режиме access
            -словарь портов в режиме trunk
      '''
      access = dict()
      trunk  = dict()
      with open(config_filename, 'r') as file:
            for i in file:
                  if i.startswith('!'):continue
                  i = i.strip(' \n')
                  if i.find('FastEthernet') != -1:
                        intf = i.split()[1]
                  elif i.find('access vlan')!= -1:
                        access[intf] = int(i.split()[-1])    
                  elif i.find('trunk allowed vlan')!= -1:
                        trunk[intf] = [int(j) for j in (i.split()[-1]).split(',')]
                  else: continue
      return (access,trunk)
         

if __name__ == '__main__':
      ports = get_int_vlan_map('config_sw1.txt')
      for i in ports:
            print(i)
