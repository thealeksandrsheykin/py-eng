# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import os
import re
import yaml
import sqlite3

DB_NAME = 'dhcp_snooping.db'


def check_exist_db(dbname):
    if not os.path.exists(dbname):
        print(f'База данных не существует. Перед добавлением данных, ее надо создать...')
        return False
    else:
        return True


def add_data(data, query):
    connection = sqlite3.connect(DB_NAME)
    for row in data:
        try:
            connection.execute(query, row)
        except sqlite3.IntegrityError as error:
            print(f'При добавлении данных: {row} Возникла ошибка: {error}')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    check_exist_db(DB_NAME)
    query_switches = 'insert into switches values(?, ?);'
    query_dhcp = 'insert into dhcp values(?, ?, ?, ?, ?);'
    with open(r'switches.yml', 'r') as file:
        switches = yaml.safe_load(file)
        data = [(switch, location) for switch, location in switches['switches'].items()]
    print(f'Добавляю данные в таблицу switches...')
    add_data(data, query_switches)
    regex = re.compile(r'(\S+) +(\S+) +.* +(\d+) +(.*)')
    files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    print(f'Добавляю данные в таблицу dhcp...')
    for file in files:
        with open(file, 'r') as f:
            switch = os.path.basename(file).split('_')[0]
            data = [i.groups() + (switch,) for i in regex.finditer(f.read())]
        add_data(data, query_dhcp)
