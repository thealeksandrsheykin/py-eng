# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию send_commands_to_devices, которая отправляет команду show или config на разные устройства в параллельных
потоках, а затем записывает вывод команд в файл.
Параметры функции:
	• devices - список словарей с параметрами подключения к устройствам
	• filename - имя файла, в который будут записаны выводы всех команд
	• show - команда show, которую нужно отправить (по умолчанию, значение None)
	• config - команды конфигурационного режима, которые нужно отправить (по умолчанию None)
    • limit - максимальное количество параллельных потоков (по умолчанию 3)
Функция ничего не возвращает. Аргументы show, config и limit должны передаваться только как ключевые. При передачи этих
аргументов как позиционных, должно генерироваться исключение TypeError.
При вызове функции send_commands_to_devices, всегда должен передаваться только один из аргументов show, config. Если передаются
оба аргумента, должно генерироваться исключение ValueError.
Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface		IP-Address		OK?		Method		Status		Protocol
Ethernet0/0		192.168.100.1	YES 	NVRAM		up			up
Ethernet0/1		192.168.200.1	YES 	NVRAM		up			up

R2#sh arp
Protocol	Address			Age (min)		Hardware Addr		Type		Interface
Internet	192.168.100.1	76				aabb.cc00.6500		ARPA		Ethernet0/0
Internet	192.168.100.2	-				aabb.cc00.6600		ARPA		Ethernet0/0
Internet	192.168.100.3	173				aabb.cc00.6700		ARPA		Ethernet0/0

R3#sh ip int br
Interface		IP-Address		OK?		Method	Status					Protocol
Ethernet0/0		192.168.100.3	YES 	NVRAM		up						up
Ethernet0/1		unassigned		YES 	NVRAM		administratively down 	down
"""
import yaml


def send_commands_to_devices(devices: dict,
                             filename: str = 'result.txt',
                             show: str = None,
                             config: list = None,
                             limit: int = 3):
    """
    The function to send different "show" commands or "config" to different devices in parallel streams and then write
    the output
    to a file.
    :param devices: list of devices with parameters of connection to them
    :param show: command string (default None)
    :param config: list of commands (default None)
    :param filename: filename to write the result
    :param limit: number of parallel thread
    :return: None
    """
    ...


if __name__ == '__main__':
    with open(r'devices.yaml', 'r') as file:
        devices = yaml.safe_load(file)
    send_commands_to_devices(devices)
