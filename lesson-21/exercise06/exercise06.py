# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import yaml,sys
sys.path.insert(1, '..\\exercise05')
from exercise05 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor


def send_and_parse_command_parallel(devices: list,
                                    command: str,
                                    templates_path: str = '\templates',
                                    limit: int = 3) -> dict:
    """
    The function for parsing command output
    :param devices: list of dictionaries with device connection parameters
    :param command: command to execute
    :param templates_path: folder where templates are stored. The default value is "templates"
    :param limit: maximum number of parallel threads (default 3)
    :return: dict:
        - keys: IP address of the device from which the output was received
        - values: list of dictionaries (output returned by the function send_and_parse_show_command)
    """
    result = dict()
    with ThreadPoolExecutor(max_workers=limit) as executor:
        for device in devices:
            result[device['host']] = (executor.submit(send_and_parse_show_command, device, command)).result()
    return result


if __name__ == '__main__':
    with open('device.yaml') as file:
        devices = yaml.safe_load(file)
        result = send_and_parse_command_parallel(devices, 'sh ip int br')
        for key, value in result.items():
            print(key, value)
