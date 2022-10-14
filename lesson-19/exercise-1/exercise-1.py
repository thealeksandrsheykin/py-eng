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


def ping_ip_addresses(ip_list, limit=3):
    """
    The function checks if IP-addresses are pinged.
    :param ip_list: list of IP-addresses
    :param limit: max numbers of parallel threads (default 3)
    :return: tuple with two lists (list of available IP-addresses, list of unavailable IP-addresses)
    """
    ...


if __name__ == '__main__':
    ip_list = []
    ping_ip_addresses(ip_list)
