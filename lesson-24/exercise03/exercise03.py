# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import yaml
from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device):
        super().__init__(**device)
        self.enable()


if __name__ == '__main__':
    with open('device.yaml') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            dev = MyNetmiko(**device)
            print(dev.send_command('sh ip int br'))
