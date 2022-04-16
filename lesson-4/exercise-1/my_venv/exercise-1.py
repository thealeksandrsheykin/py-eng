# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
change_nat = nat.replace('Fast','Gigabit')
print('{0}\n{1}'.format(nat,change_nat))

