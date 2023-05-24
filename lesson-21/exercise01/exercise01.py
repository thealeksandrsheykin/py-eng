# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import textfsm
from netmiko import ConnectHandler


def parse_command_output(template: str, command_output: str) -> list:
    """
    The function for parsing command output
    :param template: name of the file containing the TextFSM template (templates/sh_ip_int_br.template)
    :param command_output: output of the corresponding show command (str)
    :return list of two elements:
    - the first element is a list with column names
    - the remaining elements are lists in which the results of output processing are located
    """

    with open(template) as f_template:
        fsm = textfsm.TextFSM(f_template)
        header = fsm.header
        res = fsm.ParseText(output)
    return [header] + res


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
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
