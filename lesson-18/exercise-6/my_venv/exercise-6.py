# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Скопировать функцию send_config_commands из задания 5 и добавить проверку на ошибки. При выполнении каждой команды,
скрипт должен проверять результат на такие ошибки:
    • Invalid input detected
    • Incomplete command
    • Ambiguous command
Если при выполнении какой-то из команд возникла ошибка, функция должна выводить сообщение на стандартный поток вывода с
информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
    Команда «logging» выполнилась с ошибкой «Incomplete command.» на устройстве 192.168.100.1
Ошибки должны выводиться всегда, независимо от значения параметра log. При этом, log по-прежнему должен контролировать
будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1…
Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
    • первый словарь с выводом команд, которые выполнились без ошибки
    • второй словарь с выводом команд, которые выполнились с ошибками
Оба словаря в формате (примеры словарей ниже):
    • ключ - команда
    • значение - вывод с выполнением команд
Проверить работу функции можно на одном устройстве.
Списки команд с ошибками и без:
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    commands = commands_with_errors + correct_commands
'''

import yaml
import re
from netmiko import ConnectHandler
from netmiko.exceptions import AuthenticationException,SSHException

def send_config_commands(device,commands,log=False):
    '''
    Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет перечень команд в конфигурационном режиме
    на основании переданных аргументов.
    :param device: словарь с параметрами подключения к устройству
    :param config_commands: список команд, которые надо выполнить
    :return: возвращает строку с результатами выполнения команды
    '''
    command_done = {}
    command_fail = {}
    regex = r'% (?P<error>.+)'
    try:
        if log: print(f'Подключаюсь к {device["host"]}...\n')
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                result = ssh.send_config_set(command,exit_config_mode=False)
                match = re.search(regex,result)

                if match:
                    command_fail[command] = match.group("error")
                    print(f'Команда "{command}" выполнилась с ошибкой "{match.group("error")}" на устройстве: {ssh.host}')
                else:
                    command_done[command] = result
            ssh.exit_config_mode()
    except (AuthenticationException,SSHException) as error:
        print(f'{error}')
    return command_done, command_fail


if __name__ == '__main__':
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    commands = commands_with_errors + correct_commands
    with open('devices.yaml','r') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            print(f'{send_config_commands(device,commands,True)}\n'
                  f'{"-" * 80}')