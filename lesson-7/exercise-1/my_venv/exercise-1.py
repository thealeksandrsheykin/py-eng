# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


inform = list()

template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''

with open ('ospf.txt', 'r') as file:
      for i in file:
            for j in i.split():
                 data = j.strip('[,]')
                 if data == 'O':
                       data = 'OSPF'
                 elif data == 'via': continue
                 else: pass
                 inform.append(data)
            print(template.format(inform[0],inform[1],inform[2],inform[3],inform[4],inform[5]))
            inform = []
