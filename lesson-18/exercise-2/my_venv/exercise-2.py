# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
2.Скопировать функцию send_show_command из задания 1 и переделать ее таким образом, чтобы обрабатывалось исключение,
которое генерируется при ошибке аутентификации на устройстве. При возникновении ошибки, на стандартный поток вывода
должно выводиться сообщение исключения.
Для проверки измените пароль на устройстве или в файле devices.yaml.
'''

import yaml
from netmiko import ConnectHandler


def send_show_command(dev,command):
    '''
    Функция подключается по SSH к устройству и выполняет указанную команду.
    :param dev: словарь с параметрами подключения к устройству
    :param command: команда, которую надо выполнить
    :return: возвращает строку с выводом команды.
    '''
    try:
        with ConnectHandler(**dev) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    except:
        print('Произошла ошибка...')


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        for dev in devices:
            print(f'{send_show_command(dev, command)}\n'
                  f'{"-" * 80}')

