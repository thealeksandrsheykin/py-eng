# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input("Введите номер VLAN: ")

table = list()

with open('CAM_table.txt', 'r') as src_file:
      for i in src_file:
            row = i.strip('\n')
            if row.count('.') == 2:
                  vlans,mac,_,interface = row.split()
                  if vlans == vlan:
                      tmp_tuple = (int(vlans),mac,interface)
                      table.append(tmp_tuple)
                  else: pass
            else: continue
      for j in sorted(table): # sorted(table, key=lambda row:int(row[0]))
            print('{} {} {}'.format(j[0],j[1],j[2]))
