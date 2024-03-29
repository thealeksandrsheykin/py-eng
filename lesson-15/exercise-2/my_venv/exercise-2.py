# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Скопировать функцию get_ip_from_cfg из задания 1 и переделать ее таким образом, чтобы она возвращала словарь:
    • ключ:     имя интерфейса
    • значение: кортеж с двумя строками:
            – IP-адрес
            – Маска
В словарь добавлять только те интерфейсы, на которых настроены IP-адреса. Например (взяты произвольные адреса):
    {"FastEthernet0/1": ("10.0.1.1", "255.255.255.0"),"FastEthernet0/2": ("10.0.2.1", "255.255.255.0")}

Для получения такого результата, используйте регулярные выражения.Проверить работу функции на примере файла config_r1.txt.
Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса, диапазоны адресов и так далее, так как
обрабатывается вывод команды, а не ввод пользователя.
'''
import re

# 1.Способ
def get_ip_from_cfg(filename):
    '''
    Функция обрабатывает конфигурацию
    :param filename: имя файла
    :return: возвращает словарь:
                • ключ:     имя интерфейса
                • значение: кортеж с двумя строками:
                            – IP-адрес
                            – Маска
    '''
    intf_dict = dict()
    regex = r'interface +(\S+).+?ip address (\S+) +(\S+)'

    with open(filename, 'r') as file:
        for match in re.finditer(regex,file.read(), re.DOTALL):
            intf_dict[match.group(1)] = match.groups()[1:]
    return intf_dict

#2.Способ
def get_ip_from_cfg_2(filename):

    intf_dict = dict()
    regex = r'interface +(\S+).+?ip address (\S+) +(\S+)'
    with open(filename, 'r') as file:
        return {match.group(1): match.groups()[1:] for match in re.finditer(regex,file.read(), re.DOTALL)}


if __name__ == '__main__':
    print(f'1.Cпособ:')
    for i,j in (get_ip_from_cfg('config_r1.txt')).items():
        ip,mask = j
        print(f'На интерфейсе {i} настроен IP-адреc: {ip} и MASK: {mask}.')
    print(f'2.Cпособ:')
    for i,j in (get_ip_from_cfg_2('config_r1.txt')).items():
        ip,mask = j
        print(f'На интерфейсе {i} настроен IP-адреc: {ip} и MASK: {mask}.')


