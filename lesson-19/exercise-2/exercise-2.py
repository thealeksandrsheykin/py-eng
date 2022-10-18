# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Создать функцию send_show_command_to_devices, которая отправляет одну и ту же команду show на разные устройства в
параллельных потоках, а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
Параметры функции:
    • devices  - список словарей с параметрами подключения к устройствам
    • command  - команда
    • filename - имя текстового файла, в который будут записаны выводы всех команд
    • limit    - максимальное количество параллельных потоков (по умолчанию 3)
Функция ничего не возвращает. Вывод команд должен быть записан в обычный текстовый файл в таком формате (перед вы-
водом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface       IP-Address      OK?     Method  Status  Protocol
Ethernet0/0     192.168.100.1   YES     NVRAM   up      up
Ethernet0/1     192.168.200.1   YES     NVRAM   up      up

R2#sh ip int br
Interface       IP-Address      OK?     Method  Status                Protocol
Ethernet0/0     192.168.100.2   YES     NVRAM   up                    up
Ethernet0/1     10.1.1.1        YES     NVRAM   administratively down down

R3#sh ip int br
Interface       IP-Address      OK?     Method  Status                Protocol
Ethernet0/0     192.168.100.3   YES     NVRAM   up                    up
Ethernet0/1     unassigned      YES     NVRAM   administratively down down

Для выполнения задания можно создавать любые дополнительные функции.
Проверить работу функции на устройствах из файла devices.yaml

"""

import yaml
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoBaseException, NetMikoAuthenticationException)


def send_command(device: dict, command: str) -> str:
    """
    The function connection to device and sending a command to it.
    :param device: dict with parameters of device
    :param command: command string
    :return: output string
    """
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)

    except (NetMikoAuthenticationException, NetmikoBaseException, NetmikoTimeoutException) as error:
        print(error)


def send_show_command_to_devices(devices: list, command: str, filename: str = 'result.txt', limit: int = 3) -> any:
    """
    The function parallel sent one command to different devices adn write result to text file.
    :param devises: list of dict with parameters connection to devices
    :param command: command
    :param filename: the name of the text file to write the result
    :param limit: max amount thread
    :return: None
    """
    with ThreadPoolExecutor(max_workers=limit) as executor, open(filename, 'w+') as file:
        result = executor.map(send_command, devices, repeat(command))
        for device, output_command in zip(devices, result):
            file.write(f'{device["host"]}#{command}\n')
            file.write(output_command)
            file.write(f'\n------------------------\n')


if __name__ == '__main__':
    command = 'sh ip int br'
    with open('devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
    send_show_command_to_devices(devices, command)
