# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import re
import yaml
from netmiko.cisco.cisco_ios import CiscoIosSSH


class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании, возникла ошибка.
    """


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device):
        super().__init__(**device)
        self.enable()

    def send_command(self, command_string, *args, **kwargs):
        out_command = super().send_command(command_string, *args, **kwargs)
        self._check_error_in_command(command_string, out_command)
        return out_command

    def _check_error_in_command(self, command, out_command):
        regex = re.compile('% .*')
        error = re.search(regex, out_command)
        if error:
            raise ErrorInCommand(f'При выполнении команды "{command}" на устройстве {self.host} возникла ошибка '
                                 f'"{error.group(0)}"')


if __name__ == '__main__':
    with open('device.yaml') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            dev = MyNetmiko(**device)
            print(dev.send_command('sh ip int br'))
