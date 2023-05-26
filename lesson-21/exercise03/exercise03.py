# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys

sys.path.insert(1, '..//exercise01')

import exercise01

if __name__ == '__main__':
    with open(r'output//sh_ip_dhcp_snooping.txt', 'r') as file:
        res = exercise01.parse_command_output('templates//sh_ip_dhcp_snooping.template', file.read())
        print(res)
