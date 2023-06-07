# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import telnetlib, time


class CiscoTelnet:
    def __init__(self, ip: str, username: str, password: str, secret: str) -> None:
        self.ip = ip
        self.username = username
        self.password = password
        self.secret = secret
        self.telnet = telnetlib.Telnet(self.ip)

        self.telnet.read_until(b'Username')
        self.telnet.write(self._write_line(self.username))
        self.telnet.read_until(b'Password')
        self.telnet.write(self._write_line(self.password))
        flag, _, _ = self.telnet.expect([b'>', b'#'])
        if not flag:
            self.telnet.write(b'enable\n')
            self.telnet.read_until(b'Password')
            self.telnet.write(self._write_line(self.secret))
            self.telnet.read_until(b'#', timeout=5)
        self.telnet.write(b'terminal length 0\n')
        self.telnet.read_until(b'#', timeout=5)
        time.sleep(5)

    def _write_line(self, line: str) -> str:
        return f'{line}\n'.encode('utf-8')

    def send_show_command(self, command: str) -> str:
        self.telnet.write(self._write_line(command))
        return self.telnet.read_until(b'#').decode('utf-8')


if __name__ == '__main__':
    sw1 = {
        'ip': '192.168.100.1',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'}
    device = CiscoTelnet(**sw1)
    print(device.send_show_command('sh ip int br'))
