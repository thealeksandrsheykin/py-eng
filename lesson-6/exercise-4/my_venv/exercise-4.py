# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



result = True

while result:
    ip = input('Введите IP-адрес в формате A.B.C.D: ')
    data = ip.split('.')

    if len(data) == 4:
          for i in data:
                result = result & True if 0 <= int(i) <= 255 else False
          if not result:
                result = True
                print('Неправильный IP-адрес\n')
          else:
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
                result = False
    else: print('Неправильный IP-адрес\n')
