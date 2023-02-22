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
from jinja2 import FileSystemLoader, Environment

if __name__ == '__main__':
    ...