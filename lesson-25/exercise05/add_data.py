# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import os
import re
import yaml
import sqlite3
from tabulate import tabulate
from datetime import datetime


def check_exist_db(dbname):
    if not os.path.exists(dbname):
        print(f'База данных не существует. Перед добавлением данных, ее надо создать...')
        return False
    else:
        return True


def connect_to_db(dbname):
    return sqlite3.connect(dbname)


def run_query(dbname, query):
    connection = connect_to_db(dbname)
    try:
        return connection.execute(query)
    except sqlite3.IntegrityError as error:
        print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
    connection.commit()
    connection.close()



def add_data(dbname, query, data):
    connection = connect_to_db(dbname)
    for row in data:
        try:
            connection.execute(query, row)
        except sqlite3.IntegrityError as error:
            print(f'При добавлении данных: {row} Возникла ошибка: {error}')
    connection.commit()
    connection.close()


def add_data_to_table_switches(dbname, file):
    query = 'insert into switches values(?, ?);'
    with open(file, 'r') as f:
        switches = yaml.safe_load(f)
        data = [(switch, location) for switch, location in switches['switches'].items()]
        print(f'Добавляю данные в таблицу switches...')
        add_data(dbname, query, data)


def add_data_to_table_dhcp(dbname, list_dhcp_files):
    query = "replace into dhcp values(?, ?, ?, ?, ?, ?, datetime('now'));"
    regex = re.compile(r'(\S+) +(\S+) +.* +(\d+) +(.*)')
    run_query(dbname, 'update dhcp set active=0')
    print(f'Добавляю данные в таблицу dhcp...')
    for file in list_dhcp_files:
        with open(file, 'r') as f:
            switch = os.path.basename(file).split('_')[0]
            data = [i.groups() + (switch, 1) for i in regex.finditer(f.read())]
        add_data(dbname, query, data)


if __name__ == '__main__':
    dbname = 'dhcp_snooping.db'
    check_exist_db(dbname)
    add_data_to_table_switches(dbname, 'switches.yml')
    #add_data_to_table_dhcp(dbname, ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt'])
    add_data_to_table_dhcp(dbname, ['sw1_new_dhcp_snooping.txt', 'sw2_new_dhcp_snooping.txt', 'sw3_new_dhcp_snooping.txt'])
    print(tabulate(run_query(dbname, 'select * from dhcp;')))



