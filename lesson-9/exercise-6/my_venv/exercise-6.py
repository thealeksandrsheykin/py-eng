# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
                  elif i.find('access')!= -1:
                        if i.split()[-1] == 'access':
                              access[intf] = 1
                        else: access[intf] = int(i.split()[-1])    
                  elif i.find('trunk allowed vlan')!= -1:
                        trunk[intf] = [int(j) for j in (i.split()[-1]).split(',')]
                  else: continue
      return (access,trunk)
         


ports = get_int_vlan_map('config_sw2.txt')
for i in ports:
      print(i)
