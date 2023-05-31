# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import yaml
import sys
sys.path.insert(1, '..//exercise04')
from exercise04 import parse_command_dynamic
from netmiko import ConnectHandler


def send_and_parse_show_command(device_dict: dict,
                                command: str,
                                templates_path: str = 'templates',
                                index: str = 'index') -> list:
    """
    The function for parsing command output
    :param device_dict: dictionary with connection parameters to device
    :param command: command to execute
    :param templates_path: folder where templates are stored. The default value is "templates"
    :param index: the name of the file that stores the correspondence between commands and templates.
                  The default value is "index"
    :return: list of dictionaries with the results of processing the output of the comma
    """
    with ConnectHandler(**device_dict) as telnet:
        telnet.enable()
        output = telnet.send_command(command)
        return parse_command_dynamic(output, {'command': command})


if __name__ == '__main__':
    with open('device.yaml') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            result = send_and_parse_show_command(device, 'show ip int brief')
            print(result)
