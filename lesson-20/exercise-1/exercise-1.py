# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
Создать функцию generate_config.
Параметры функции:
    • template - путь к файлу с шаблоном (например, «templates/for.txt»)
    • data_dict - словарь со значениями, которые надо подставить в шаблон
Функция должна возвращать строку с конфигурацией, которая была сгенерирована.
Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.
"""
import yaml

def generate_config(template: str, data_dict: dict) -> str:
    """
    This function should return a string with the configuration.
    :param template: path to file with template
    :param data_dict: dictionary with values to be substituded into the template
    :return: string with configuration
    """
    ...


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load()
    print(generate_config(template_file, data))
