# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
6.Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:

Network:
10       1        1        0
00001010 00000001 00000001 00000000

Mask:
/24
255      255      255      0
11111111 11111111 11111111 00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
"1" * 28 + "0" * 4
"11111111111111111111111111110000"

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input('Введите IP-сеть в формате: A.B.C.D/L: ')

ip,length = network.split('/')

octets = ip.split('.')
mask_bin = '1' * int(length) + '0' * (32-int(length))


template_ip = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}'''

template_mask = '''
Mask:
/{}
{:<8} {:<8} {:<8} {:<8}  
{:<8} {:<8} {:<8} {:<8}
'''

print(template_ip.format(octets[0],     octets[1],      octets[2],      octets[3],
                     int(octets[0]),int(octets[1]), int(octets[2]), int(octets[3])))

print(template_mask.format(length,int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2),
                               mask_bin[0:8],       mask_bin[8:16],       mask_bin[16:24],       mask_bin[24:32]))


