# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import sqlite3
from tabulate import tabulate


def connect_to_db(db):
    connection = sqlite3.connect(db)
    return connection


def run_query(connect, query):
    try:
        return connect.execute(query)
    except sqlite3.IntegrityError as error:
        print(f'Возникла ошибка: {error}')


def check_parameters(parameter):
    parameters = ('mac', 'ip', 'vlan', 'interface', 'switch')
    if not parameter in parameters:
        print(f'Данный параметр {parameter} не поддерживается.\n'
              f'Допустимые значения параметров: mac, ip, vlan, interface, switch')
        return False
    else:
        return True


def print_result(data):
    print(tabulate(data))


if __name__ == '__main__':
    dbname = 'dhcp_snooping.db'
    query_general = 'select * from dhcp'
    query_with_param = 'select * from dhcp where {} = "{}"'

    args = sys.argv[1:]
    if not args:
        print('В таблице dhcp такие записи: ')
        print_result(run_query(connect_to_db(dbname), query_general))
    elif len(args) == 2 and check_parameters(args[0]):
        print(f'Информация об устройствах с такими параметрами: {args[0]} {args[1]}')
        print_result(run_query(connect_to_db(dbname), query_with_param.format(*args)))
    else:
        print('Пожалуйста, введите два или ноль аргументов')
