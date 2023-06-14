# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import telnetlib

import yaml, time
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

    def send_config_commands(self, commands: any) -> str:
        output = str()
        if isinstance(commands, str):
            commands = [commands]
        commands = ['conf t', *commands, 'end']  # f'conf t,{",".join(commands)},end'.split(',')
        for command in commands:
            self.telnet.write(self._write_line(command))
            output += f"{self.telnet.read_until(b'#', timeout=5).decode('utf-8')}\n"
        return output


if __name__ == '__main__':
    with open('devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            result = CiscoTelnet(**device).send_config_commands(
                ['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
            print(result)
