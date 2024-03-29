# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

template = '''
Protocol:           {}
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}'''

protocol,prefix,admetric,_,nexthop,lastupdate,outinterface = ospf_route.split()
protocol = protocol + 'SPF'
admetric = admetric.strip('[]')

print(template.format(protocol,prefix,admetric,nexthop,lastupdate,outinterface))

