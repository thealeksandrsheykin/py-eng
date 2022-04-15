# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''



network = input('Введите IP-ceть в формате A.B.C.D/Length: ' )


template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{4:}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:<08b} {6:<08b} {7:<08b} {8:<08b}
'''

ip,mask = network.split('/')
#ip enter
ipoct1,ipoct2,ipoct3,ipoct4 = ip.split('.')
#mask
mask_bin = '1'*int(mask) + '0'*(32-int(mask))
maskoct1 = int(mask_bin[0:8],  2)
maskoct2 = int(mask_bin[8:16], 2)
maskoct3 = int(mask_bin[16:24],2)
maskoct4 = int(mask_bin[24:],  2)
#ip network
ipoct1 = int(bin(int(ipoct1)& maskoct1),2)
ipoct2 = int(bin(int(ipoct2)& maskoct2),2)
ipoct3 = int(bin(int(ipoct3)& maskoct3),2)
ipoct4 = int(bin(int(ipoct4)& maskoct4),2)


print(template.format(ipoct1,   ipoct2,   ipoct3,   ipoct4, mask,
                      maskoct1, maskoct2, maskoct3, maskoct4))
