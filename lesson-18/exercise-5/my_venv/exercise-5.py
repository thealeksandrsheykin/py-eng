# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Скопировать функцию send_config_commands из задания 4 и добавить параметр log, который контролирует будет ли выводится
на стандартный поток вывода информация о том к какому устройству выполняется подключение. По умолчанию, результат должен
выводиться. Пример работы функции:
    result = send_config_commands(r1, commands)
    Подключаюсь к 192.168.100.1...
    result = send_config_commands(r1, commands, log=False)
Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
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
            return ssh.send_config_set(commands)
    except (AuthenticationException,SSHException) as error:
        print(f'{error}')


if __name__ == '__main__':
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    with open('devices.yaml','r') as file:
        devices = yaml.safe_load(file)
        for device in devices:
            print(f'{send_config_commands(device,commands)}\n'
                  f'{"-" * 80}')
