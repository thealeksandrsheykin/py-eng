# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import os
import sqlite3


def create_db(dbname):
    if not os.path.exists(dbname):
        print(f'Создаю базу данных {dbname}...')
        connect = sqlite3.connect(dbname)
    else:
        print(f'База данных {dbname} существует...')
        return 0
    with open(r'dhcp_snooping_schema.sql', 'r') as file:
        schema = file.read()
    connect.executescript(schema)
    connect.commit()
    connect.close()


if __name__ == '__main__':
    create_db('dhcp_snooping.db')
