# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from textfsm import clitable
from netmiko import ConnectHandler


def parse_command_dynamic(command_output: str,
                          attributes_dict: dict,
                          index_file: str = 'index',
                          templ_path: str = 'templates') -> list:
    """
    The function for parsing command output
    :param command_output: output of the corresponding show command (str)
    :param attributes_dict: an attribute dictionary containing the following key-value pairs:
                            "command": command
                            "vendor": vendor
    :param index_file: the name of the file that stores the correspondence between commands and templates.
                       The default value is "index".
    :param templ_path: folder where templates are stored. The default value is "templates"
    :return: list of dictionaries with the results of processing the output of the command
    """
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, data)) for data in cli_table]


if __name__ == '__main__':
    device = {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.100.1",
        "username": "admin",
        "password": "cisco",
        "secret": "cisco",
    }

    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command("sh ip int br")
    attributes = {"Command": "show ip int br", "Vendor": "cisco"}
    result = parse_command_dynamic(output, attributes)
    print(result)
