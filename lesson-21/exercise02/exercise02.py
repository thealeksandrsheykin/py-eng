# -*- coding: utf-8 -*_
# !/usr/bin/env python3

import textfsm
from netmiko import ConnectHandler


def parse_output_to_dict(template: str, command_output: str) -> list:
    """
    The function for parsing command output
    :param template: name of the file containing the TextFSM template (templates/sh_ip_int_br.template)
    :param command_output: output of the corresponding show command (str)
    :return dict:
    - keys - variable names in the TextFSM template
    - values - parts of the output that correspond to the variables
    """
    with open(template) as file_template:
        fsm = textfsm.TextFSM(file_template)
        return fsm.ParseTextToDicts(command_output)


if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.100.1",
        "username": "admin",
        "password": "cisco",
        "secret": "cisco",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    print(result)
