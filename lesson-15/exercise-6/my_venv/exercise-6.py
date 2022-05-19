# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
Функция ожидает такие аргументы:
    • имя файла, в котором находится правила NAT Cisco IOS
    • имя файла, в который надо записать полученные правила NAT для ASA
Функция ничего не возвращает. Проверить функцию на файле cisco_nat_config.txt.
Пример правил NAT cisco IOS:
    ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
    ip nat inside source static tcp 10.1.9.5  22 interface GigabitEthernet0/1 20023
И соответствующие правила NAT для ASA:
    object network LOCAL_10.1.2.84
        host 10.1.2.84
        nat (inside,outside) static interface service tcp 22 20022
    object network LOCAL_10.1.9.5
        host 10.1.9.5
        nat (inside,outside) static interface service tcp 22 20023
В файле с правилами для ASA:
    • не должно быть пустых строк между правилами
    • перед строками «object network» не должны быть пробелы
    • перед остальными строками должен быть один пробел
Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
import re
from datetime import datetime

# 1. Cпособ
def convert_ios_nat_to_asa(file_in,file_out):
    '''
    Функция конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
    :param file_in: имя файла, в котором находится правила NAT Cisco IOS
    :param file_out: имя файла, в который надо записать полученные правила NAT для ASA
    :return: функция ничего не возвращает
    '''
    template = '''object network LOCAL_{}\n\thost {}\n\tnat (inside,outside) static interface service tcp {} {}\n'''
    with open (file_in, 'r') as data, open(file_out ,'w') as result:
        for match in re.finditer(r'([\d+.]+) +(\d+) .* +(\d+)',data.read()):
            rule = [match.group(1)] + list(match.groups())
            result.write(template.format(*rule))

# 2.Способ
def convert_ios_nat_to_asa_2(file_in,file_out):
    template = ('object network LOCAL_{ip}\n'
                '\thost {ip}\n'
                '\tnat (inside,outside) static interface service tcp {lport} {gport}\n')
    with open (file_in, 'r') as data, open(file_out ,'w') as result:
        for match in re.finditer(r'(?P<ip>[\d+.]+) +(?P<lport>\d+) .* +(?P<gport>\d+)',data.read()):
            result.write(template.format(**match.groupdict()))


if __name__ == '__main__':
    date = "{:%d_%B_%Y}".format(datetime.now())
    convert_ios_nat_to_asa_2('cisco_nat_config.txt', f'ASA_{date}.txt')

