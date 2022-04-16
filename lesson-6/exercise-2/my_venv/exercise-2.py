# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Введите IP-адрес в формате A.B.C.D: ')

if   ip == '0.0.0.0':
      print('IP адрес {} - unassigned'.format(ip))
elif ip == '255.255.255.255':
      print('IP адрес {} - local broadcast'.format(ip))
elif 223 >= int(ip.split('.')[0]) >=1:
      print('IP адрес {} - unicast'.format(ip))
elif 239 >= int(ip.split('.')[0]) >= 224:
      print('IP адрес {} - multicast'.format(ip))
else:
      print('IP адрес {} - unused'.format(ip))
      

