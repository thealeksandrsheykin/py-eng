# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
1.Используя подготовленную строку nat, получить новую строку, в которой в имени интерфейса вместо FastEthernet написано
GigabitEthernet. Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
Ограничение: Все задания надо выполнять используя только пройденные темы.

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(f'{nat.replace("Fast","Gigabit")}')
