# -*-coding: utf-8-*-
# !/usr/bin/env python3

"""
Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса. Проверка IP-адресов должна выполняться
параллельно в разных потоках. Параметры функции:
    • ip_list - список IP-адресов
    • limit   - максимальное количество параллельных потоков (по умолчанию 3)
Функция должна возвращать кортеж с двумя списками:
    • список доступных IP-адресов
    • список недоступных IP-адресов
Для выполнения задания можно создавать любые дополнительные функции. Для проверки доступности IP-адреса, используйте
ping.
Примечание:
Подсказка о работе с concurrent.futures: Если необходимо пинговать несколько IP-адресов в разных потоках, надо
создать функцию, которая будет пинговать один IP-адрес, а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor


def send_icmp_to_host(host: str, number: str = '1') -> int:
    """
    The function send a ping
    :param number: string number of requests ping
    :param host: string with address or hostname
    :return: code (0 if address is available or 1 if vice versa)
    """
    start_msg = '===> Send icmp echo request to: {}'
    received_msg = '<=== Received icmp echo reply from {} code: {}'
    logging.info(start_msg.format(host))
    result = subprocess.run(['ping', '-c', number, host], stdout=subprocess.DEVNULL).returncode
    logging.info(received_msg.format(host, result))
    return result


def ping_ip_addresses(ip_list: list, limit=3) -> tuple:
    """
    The function checks if IP-addresses are pinged.
    :param ip_list: list of IP-addresses
    :param limit: max numbers of parallel threads (default 3)
    :return: tuple with two lists (list of available IP-addresses, list of unavailable IP-addresses)
    """
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_icmp_to_host, ip_list)
        for device, output in zip(ip_list, result):
            print(f'Device: {device} -> {"DONE" if not output else "FAILED"}')


if __name__ == '__main__':
    logging.basicConfig(format='%(threadName)s %(name)s %(levelname)s: %(message)s',
                        level=logging.INFO,)
    ip_list = ['172.18.73.18', '172.21.73.254', '172.22.73.254', '172.23.73.254']
    ping_ip_addresses(ip_list)
