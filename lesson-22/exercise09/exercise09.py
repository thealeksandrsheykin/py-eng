# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import telnetlib
import re
import time
import yaml
from textfsm import clitable


class CiscoTelnet:
    def __init__(self, ip: str, username: str, password: str, secret: str) -> None:
        self.ip = ip
        self.username = username
        self.password = password
        self.secret = secret
        self.telnet = telnetlib.Telnet(self.ip)

        self.telnet.read_until(b'Username', timeout=5)
        self.telnet.write(self._write_line(self.username))
        self.telnet.read_until(b'Password', timeout=5)
        self.telnet.write(self._write_line(self.password))
        flag, _, _ = self.telnet.expect([b'>', b'#'])
        if not flag:
            self.telnet.write(b'enable\n')
            self.telnet.read_until(b'Password', timeout=5)
            self.telnet.write(self._write_line(self.secret))
            self.telnet.read_until(b'#', timeout=5)
        self.telnet.write(b'terminal length 0\n')
        self.telnet.read_until(b'#', timeout=5)
        time.sleep(5)

    def _write_line(self, line: str) -> str:
        return f'{line}\n'.encode('utf-8')

    def send_show_command(self, command: str,
                          parse: bool = True,
                          templates: str = 'templates',
                          index: str = 'index') -> any:

        self.telnet.write(self._write_line(command))
        time.sleep(5)
        output = self.telnet.read_until(b'#', timeout=5).decode('utf-8')
        if parse:
            cli_table = clitable.CliTable(index, templates)
            cli_table.ParseCmd(output, {"Command": command, "Vendor": "cisco"})
            return [dict(zip(cli_table.header, data)) for data in cli_table]
        else:
            return output

    def send_config_commands(self, commands: any, strict: bool = True) -> str:
        regex = r"%(.*)"
        output = str()
        message = ('При выполенении команды "{}" на устройстве {} ' \
                   'возникла ошибка -> {}')
        if isinstance(commands, str):
            commands = [commands]
        commands = ['conf t', *commands, 'end']
        for command in commands:
            self.telnet.write(self._write_line(command))
            result = self.telnet.read_until(b'#', timeout=5).decode('utf-8')
            error_in_command = re.findall(regex, result)
            if error_in_command and not strict:
                print(message.format(command, self.telnet.host, error_in_command[0]))
            elif error_in_command and strict:
                raise ValueError(message.format(command, self.telnet.host, error_in_command[0]))
            output += result
        return output


if __name__ == '__main__':
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    commands = commands_with_errors + correct_commands
    with open('devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            result = CiscoTelnet(**device).send_config_commands(commands, strict=False)
            print(result)
