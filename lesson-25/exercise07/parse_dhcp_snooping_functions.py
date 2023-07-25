# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import re
import sqlite3
import yaml
from tabulate import tabulate


def create_db(name, schema):
    if not os.path.exists(name):
        connect = sqlite3.connect(name)
    else:
        print(f'База данных {name} существует...')
        return 0
    with open(schema, 'r') as file:
        sql_schema = file.read()
    connect.executescript(sql_schema)
    connect.commit()
    connect.close()


def run_query_with_data(db_file, query, data):
    with sqlite3.connect(db_file) as connection:
        for i in data:
            try:
                connection.execute(query, i)
            except sqlite3.IntegrityError as error:
                print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
            finally:
                connection.commit()


def run_query_simple(db_file, query):
    with sqlite3.connect(db_file) as connection:
        try:
            return connection.execute(query)
        except sqlite3.IntegrityError as error:
            print(f'При выполнении запроса: {query} Возникла ошибка: {error}')
        finally:
            connection.commit()


def add_data_switches(db_file, filename):
    query = 'insert into switches values(?, ?);'
    with open(filename[0], 'r') as f:
        switches = yaml.safe_load(f)
        data = [(switch, location) for switch, location in switches['switches'].items()]
        print(f'Добавляю данные в таблицу switches...')
        run_query_with_data(db_file, query, data)


def add_data(db_file, filename):
    query = 'replace into dhcp values(?, ?, ?, ?, ?, ?, datetime("now"));'
    regex = re.compile(r'(\S+) +(\S+) +.* +(\d+) +(.*)')
    run_query_simple(db_file, 'update dhcp set active=0')
    for file in filename:
        with open(file, 'r') as f:
            switch = os.path.basename(file).split('_')[0]
            data = [i.groups() + (switch, 1) for i in regex.finditer(f.read())]
        run_query_with_data(db_file, query, data)


def get_data(db_file, key, value):
    state = {'активные': 1, 'неактивные': 0}
    query = f'select * from dhcp where {key} = "{value}"' + ' and active = {}'
    for i in state:
        result = list(run_query_simple(db_file, query.format(state[i])))
        if result:
            print(f'{i.capitalize()} записи:\n{tabulate(result)}')


def get_all_data(db_file):
    print(tabulate(run_query_simple(db_file, 'select * from dhcp;')))


