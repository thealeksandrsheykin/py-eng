# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию send_command_to_devices, которая отправляет разные команды show на разные устройства в параллельных
потоках, а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
Параметры функции:
    • devices - список словарей с параметрами подключения к устройствам
    • commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
    • filename - имя файла, в который будут записаны выводы всех команд
    • limit - максимальное количество параллельных потоков (по умолчанию 3)
Функция ничего не возвращает. Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо
написать имя хоста и саму команду):
R1#sh ip int br
Interface       IP-Address      OK?     Method      Status      Protocol
Ethernet0/0     192.168.100.1   YES     NVRAM       up          up
Ethernet0/1     192.168.200.1   YES     NVRAM       up          up

R2#sh arp
Protocol        Address         Age (min)       Hardware Addr       Type        Interface
Internet        192.168.100.1   76              aabb.cc00.6500      ARPA        Ethernet0/0
Internet        192.168.100.2   -               aabb.cc00.6600      ARPA        Ethernet0/0
Internet        192.168.100.31  73              aabb.cc00.6700      ARPA        Ethernet0/0

R3#sh ip int br
Interface       IP-Address      OK?     Method      Status                  Protocol
Ethernet0/0     192.168.100.3   YES     NVRAM       up                      up
Ethernet0/1     unassigned      YES     NVRAM       administratively down   down

Для выполнения задания можно создавать любые дополнительные функции. Проверить работу функции на устройствах из файла
devices.yaml и словаре commands:

commands = {
    "192.168.100.3": "sh run | s ^router ospf",
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh int desc",
}
"""

import yaml
from concurrent.futures import ThreadPoolExecutor
from netmiko import (ConnectHandler, NetmikoBaseException, NetmikoTimeoutException, NetMikoAuthenticationException)


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
    except (NetmikoBaseException, NetmikoTimeoutException, NetMikoAuthenticationException) as error:
        print(error)


def send_command_to_device(devices: list, commands_dict: dict, filename: str = 'result.txt', limit: int = 3) -> None:
    """
    The function to send different "Show" commands to different devices in parallel streams and then write the output
    to a file.
    :param devices: list of devices with parameters of connection to them
    :param commands_dict: dict with information about which device to send which command
    :param filename: filename to write the result
    :param limit: number of parallel thread
    :return: None
    """
    ...


if __name__ == '__main__':
    commands = {
        "172.16.5.32": "sh run | s ^router ospf",
        "172.16.5.36": "sh ip int br",
        "172.16.5.40": "sh int desc",
    }
    with open('devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
        send_command_to_device(devices, commands)
