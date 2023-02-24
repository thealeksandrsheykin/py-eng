# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Создать шаблон templates/cisco_router_base.txt. В шаблон templates/cisco_router_base.txt должно быть включено
содержимое шаблонов:
    • templates/cisco_base.txt
    • templates/alias.txt
    • templates/eem_int_desc.txt
При этом, нельзя копировать текст шаблонов. Проверьте шаблон templates/cisco_router_base.txt, с помощью функции
generate_config из задания 1. Не копируйте код функции generate_config. В качестве данных, используйте информацию
из файла data_files/router_info.yml
"""

import os
import yaml
from exercise01 import generate_config


def merge_templates(templates: list, template_file: str) -> None:
    """
    This function merge templates into one.
    :param templates: list of template names
    :param template_file: resulting filename
    :return: None
    """
    with open(template_file, 'w') as f:
        for template in templates:
            f.write("{{% include '{0}' %}}\n".format(template))


if __name__ == '__main__':
    data_file = "data_files/router_info.yml"
    template_file = "templates/cisco_router_base.txt"
    merge_templates(os.listdir('templates'), template_file)
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
