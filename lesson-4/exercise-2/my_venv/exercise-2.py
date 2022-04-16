# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
mac_change =mac.replace(':','.')

print(f'{mac}\n{mac_change}')
