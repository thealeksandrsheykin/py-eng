# -*- coding: utf-8 -*-
# !/usr/bin/env python3


import yaml
from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device):
        super().__init__(**device)
        self.ssh.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        self.ssh.close()


if __name__ == '__main__':
    with open('device.yaml') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            dev = CiscoSSH(**device)
            print(dev.send_show_command('show ip int br'))

