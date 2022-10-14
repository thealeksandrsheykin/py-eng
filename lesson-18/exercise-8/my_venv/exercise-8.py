# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Создать функцию send_commands (для подключения по SSH используется netmiko).
Параметры функции:
    • device - словарь с параметрами подключения к одному устройству
    • show - одна команда show (строка)
    • config - список с командами, которые надо выполнить в конфигурационном режиме
Аргументы show и config должны передаваться только как ключевые. При передачи этих аргументов как позиционных, должно
генерироваться исключение TypeError.
В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри. При вызове функции send_commands,
всегда должен передаваться только один из аргументов show, config. Если передаются оба аргумента, должно генерироваться
исключение ValueError.
Далее комбинация из аргумента и соответствующей функции:
    • show - функция send_show_command из задания 1
    • config - функция send_config_commands из задания 2
Функция возвращает строку с результатами выполнения команд или команды.
Проверить работу функции:
    • со списком команд commands
    • командой command
'''

import yaml
from netmiko.exceptions import SSHException,AuthenticationException
from netmiko import ConnectHandler

from exercise_1 import send_show_command
from exercise_4 import send_config_commands

def send_commands(device,*,show=None,config=None):
    '''
    Функция возвращает строку с результатами выполнения команд или команды.
    :param device: словарь с параметрами подключения к одному устройству
    :param show: одна команда show (строка)
    :param config: список с командами, которые надо выполнить в конфигурационном режиме
    :return: возвращает строку с результатами выполнения команд или команды
    '''

    if show and config:
        raise ValueError('Функция принимает только один из аргументов "show" или "config"...')
    elif show:
        return send_show_command(device,show)
    elif config:
        return send_config_commands(device,config)
    else:
        raise ValueError('Функция должна принимать одно из значений "show" или "config"...')

if __name__ == '__main__':
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    command = 'sh ip int br'
    with open('devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
    print(f'Устройство: {devices[0]["host"]}\n'
          f'Команда: "{command}"\n'
          f'Вывод:\n'
          f'{send_commands(devices[0], show=command)}\n'
          f'{"-" * 80}\n'
          f'Устройство: {devices[1]["host"]}\n'
          f'Список команд: {commands}\n'
          f'Вывод:\n'
          f'{send_commands(devices[0],config=commands)}\n')
