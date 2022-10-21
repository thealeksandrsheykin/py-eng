# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию send_command_to_devices, которая отправляет список указанных команд show на разные устройства в
параллельных потоках, а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.
Параметры функции:
    • devices - список словарей с параметрами подключения к устройствам
    • commands_dict - словарь в котором указано на какое устройство отправлять какие команды.
      Пример словаря - commands
    • filename - имя файла, в который будут записаны выводы всех команд
    • limit - максимальное количество параллельных потоков (по умолчанию 3)
Функция ничего не возвращает. Вывод команд должен быть записан в файл в таком формате (перед выводом каждой команды
надо написать имя хоста и саму команду):

R2#sh arp
Protocol        Address             Age (min)       Hardware Addr       Type        Interface
Internet        192.168.100.1       87              aabb.cc00.6500      ARPA        Ethernet0/0
Internet        192.168.100.2       -               aabb.cc00.6600      ARPA        Ethernet0/0

R1#sh ip int br
Interface       IP-Address      OK?      Method      Status     Protocol
Ethernet0/0     192.168.100.1   YES      NVRAM       up         up
Ethernet0/1     192.168.200.1   YES      NVRAM       up         up

R1#sh arp
Protocol        Address     Age (min)       Hardware Addr       Type        Interface
Internet        10.30.0.1   -               aabb.cc00.6530      ARPA        Ethernet0/3.300
Internet        10.100.0.1  -               aabb.cc00.6530      ARPA        Ethernet0/3.100

R3#sh ip int br
Interface       IP-Address      OK?     Method      Status                  Protocol
Ethernet0/0     192.168.100.3   YES     NVRAM       up                      up
Ethernet0/1     unassigned      YES     NVRAM       administratively down   down

R3#sh ip route | ex -

Gateway of last resort is not set
    10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O   10.1.1.1/32  [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O   10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0

Порядок команд в файле может быть любым. Для выполнения задания можно создавать любые дополнительные функции,
а также использовать функции созданные в предыдущих заданиях. Проверить работу функции на устройствах из файла
devices.yaml и словаре commands.

commands = {
"192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
"192.168.100.1": ["sh ip int br", "sh int desc"],
"192.168.100.2": ["sh int desc"],
}
"""

import yaml
from concurrent.futures import ThreadPoolExecutor
from netmiko import (ConnectHandler, NetmikoBaseException, NetmikoTimeoutException, NetMikoAuthenticationException)


def send_command(device: dict, commands: list) -> str:
    """
    The function connection to device and sending a command to it.
    :param device: dict with parameters of device
    :param commands: list of commands
    :return: output string
    """
    result = ''
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                result += f'\n------------------------\n'
                result += f'{device["host"]}#{command}\n'
                result += ssh.send_command(command)
            return result
    except (NetmikoBaseException, NetmikoTimeoutException, NetMikoAuthenticationException) as error:
        print(error)


def send_command_to_devices(devices: dict, commands_dict: dict, filename: str = 'result.txt', limit: int = 3) -> None:
    """
    The function to send  list of different "Show" commands to different devices in parallel streams and then write
    the output to a file.
    :param devices: list of devices with parameters of connection to them
    :param commands_dict: dict with information about which device to send which command
    :param filename: filename to write the result
    :param limit: number of parallel thread
    :return: None
    """
    with ThreadPoolExecutor(max_workers=limit) as executor, open(filename, 'w+') as file:
        for device in devices:
            output = executor.submit(send_command, device, commands_dict[device['host']])
            file.write(f'{output.result()}')


if __name__ == '__main__':
    commands = {
        "172.16.5.32": ["sh ip int br", "sh ip route | ex -"],
        "172.16.5.36": ["sh ip int br", "sh int desc"],
        "172.16.5.40": ["sh int desc"],
    }
    with open(r'devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
    send_command_to_devices(devices, commands)


