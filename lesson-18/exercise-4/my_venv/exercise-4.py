# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
4.Создать функцию send_config_commands
Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет перечень команд в конфигурационном режиме
на основании переданных аргументов.
Параметры функции:
    • device - словарь с параметрами подключения к устройству
    • config_commands - список команд, которые надо выполнить
Функция возвращает строку с результатами выполнения команды:
    DEVICE = {'device_type': 'cisco_ios',
              'ip':          '192.168.100.1',
              'username':    'cisco',
              'password':    'cisco',
              'secret':      'cisco'}
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    result = send_config_commands(r1, commands)
    print(result)
        config term
        Enter configuration commands, one per line. End with CNTL/Z.
        R1(config)#logging 10.255.255.1
        R1(config)#logging buffered 20010
        R1(config)#no logging console
        R1(config)#end
        R1#
Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_config_commands.
commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
'''

import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import AuthenticationException,SSHException

def send_config_commands(device,config_commands):
    '''
    Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет перечень команд в конфигурационном режиме
    на основании переданных аргументов.
    :param device: словарь с параметрами подключения к устройству
    :param config_commands: список команд, которые надо выполнить
    :return: возвращает строку с результатами выполнения команды
    '''
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
    except (AuthenticationException,SSHException) as error:
        print(f'{error}')


if __name__ == '__main__':
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    with open('devices.yaml','r') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            print(f'{send_config_commands(device,commands)}')

