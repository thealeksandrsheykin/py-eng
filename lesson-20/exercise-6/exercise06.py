# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Создать функцию configure_vpn, которая использует шаблоны из задания 5 для настройки VPN на маршрутизаторах на основе
данных в словаре data. Параметры функции:
    • src_device_params - словарь с параметрами подключения к устройству
    • dst_device_params - словарь с параметрами подключения к устройству
    • src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
    • dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
    • vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны
Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве с помощью netmiko. Функция возвращает вывод
с набором команд с двух марушртизаторов (вывод,которые возвращает метод netmiko send_config_set).При этом, в словаре data
не указан номер интерфейса Tunnel, который надо использовать. Номер надо определить самостоятельно на основе информации с
оборудования. Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер, но
одинаковый для двух маршрутизаторов. Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4. А на маршру
тизаторе dest такие: Tunnel2, Tunnel3, Tunnel8. Первый свободный номер одинаковый для двух маршрутизаторов будет 5. И на
до будет настроить интерфейс Tunnel 5.
"""
import yaml
from exercise05 import create_vpn_config
from netmiko import ConnectHandler


def configure_vpn(src_device_params: dict, dst_device_params: dict, src_template: str, dst_template: str,
                  vpn_data_dict: dict) -> None:
    """
    The function configures vpn based on template and data on each device.
    :param src_device_params: dictionary with parameters connection to device
    :param dst_device_params: dictionary with parameters connection to device
    :param src_template: filename template for first side
    :param dst_template: filename template for second side
    :param vpn_data_dict: dictionary with values to replace in the template
    :return: None
    """
    src_config_vpn, dst_config_vpn = create_vpn_config(src_template, dst_template, vpn_data_dict)
    with ConnectHandler(**src_device_params) as src_device, ConnectHandler(**dst_device_params) as dst_device:
        src_device.enable()
        dst_device.enable()


if __name__ == '__main__':
    src_template = 'templates/gre_ipsec_vpn_1.txt'
    dst_template = 'templates/gre_ipsec_vpn_2.txt'
    data = {
        'tun_num': None,
        'wan_ip_1': '192.168.100.1',
        'wan_ip_2': '192.168.100.2',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    with open('devices.yaml') as f:
        src_device, dst_device = yaml.safe_load(f)
    configure_vpn(src_device, dst_device, src_template, dst_template, data)
