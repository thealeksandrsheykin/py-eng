# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IPадресов.
Функция ожидает как аргументы два списка:
    • список доступных IP-адресов
    • список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:
    Reachable   Unreachable
    ----------- -------------
    10.1.1.1    10.1.1.7
    10.1.1.2    10.1.1.8
    10.1.1.9
'''
from itertools import zip_longest
from tabulate import tabulate

def print_ip_table(reach, unreach):
    '''
    Функция отображает таблицу доступных и недоступных IPадресов
    :param reach_list:список доступных IP-адресов
    :param unreach_list: список недоступных IP-адресов
    :return: None
    '''
    headers = ['Reachable', 'Unreachable']
    combined_list = list(zip_longest(reach,unreach))
    print(tabulate(combined_list,headers=headers,tablefmt='grid',stralign='center'))

if __name__ == '__main__':
    reach = ['10.1.1.1','10.1.1.2','10.1.1.9']
    unreach = ['10.1.1.7','10.1.1.8']
    print_ip_table(reach,unreach)
