# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
    Prefix 10.0.24.0/24
    AD/Metric 110/41
    Next-Hop 10.0.13.3
    Last update 3d18h
    Outbound Interface FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
"""

ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_list = ospf_route.split()

print(f'Prefix              {ospf_list[0].strip()}\n'
      f'AD/Metric           {ospf_list[1].strip("[]")}\n'
      f'Next-Hop            {ospf_list[3].strip(",")}\n'
      f'Last update         {ospf_list[4].strip(",")}\n'
      f'Outbound Interface  {ospf_list[5].strip()}\n')
