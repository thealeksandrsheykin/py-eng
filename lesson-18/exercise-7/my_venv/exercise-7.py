# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
7.Скопировать функцию send_config_commands из задания 6 и переделать ее таким образом: Если при выполнении команды
возникла ошибка, спросить пользователя надо ли выполнять остальные команды. Варианты ответа [y]/n:
    • y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
    • n или no - не выполнять остальные команды
Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
    • первый словарь с выводом команд, которые выполнились без ошибки
    • второй словарь с выводом команд, которые выполнились с ошибками
Оба словаря в формате
• ключ - команда
• значение - вывод с выполнением команд
Проверить работу функции можно на одном устройстве.
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
                    flag = input('Продолжать выполнять команды? [y]/n:')
                    if flag in ('n','no'):
                        break
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