# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Дополнить скрипт из задания 8 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в
запросе о номере VLANа или списка VLANов:
• для access: «Введите номер VLAN:»
• для trunk: «Введите разрешенные VLANы:»

Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без
использования условия if и циклов for/while.

access_template = [
"switchport mode access", "switchport access vlan {}",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]

trunk_template = [
"switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"
]

"""

access_template = [
"switchport mode access", "switchport access vlan {}",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]

trunk_template = [
"switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"
]

template = {'access':access_template, 'trunk':trunk_template}
question = {'access':'Введите номер VLAN: ','trunk':'Введите разрешенные VLANы: '}

mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
vlans = input(question[mode])


print(f'interface {interface}')
print('\n'.join(template[mode]).format(vlans))

