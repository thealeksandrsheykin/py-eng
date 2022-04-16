# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Введите IP-адрес в формате A.B.C.D: ')

data = ip.split('.')
result = True
if len(data) == 4:
      for i in data:
            result = result & True if 0 <= int(i) <= 255 else False
      if not result: print('Неправильный IP-адрес')
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
else: print('Неправильный IP-адрес')

