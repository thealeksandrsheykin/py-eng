# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import re


class IPAddress:
    def __init__(self, host):
        temp_data = host.split('/')
        self._check_ip(temp_data[0])
        self._check_mac(temp_data[1])
        self.ip, self.mask = temp_data[0], int(temp_data[1])

    def _check_ip(self, ip):
        regex = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
        try:
            re.search(regex, ip).group()
        except AttributeError:
            raise ValueError('Incorrect IPv4')

    def _check_mac(self, mask):
        regex = re.compile(r'^([8-9]|[12][0-9]|3[02])$')
        try:
            re.search(regex, mask).group()
        except AttributeError:
            raise ValueError('Incorrect MASK')

    def __str__(self):
          return f'IP address {self.ip}/{self.mask}'

    def __repr__(self):
         return f'IPAddress("{self.ip}/{self.mask}")'


if __name__ == '__main__':
    ip1 = IPAddress('10.1.1.1/24')
    str(ip1)
    print(ip1)
    ip_list = list()
    ip_list.append(ip1)
    print(ip_list)
