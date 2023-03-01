# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Создайте шаблон templates/ospf.txt на основе конфигурации OSPF в файле cisco_ospf.txt. Пример конфигурации дан, чтобы
показать синтаксис. Шаблон надо создавать вручную, скопировав части конфига в соответствующий шаблон. Какие значения
должны быть переменными:
    • номер процесса. Имя переменной - process
    • router-id. Имя переменной - router_id
    • reference-bandwidth. Имя переменной - ref_bw
    • интерфейсы, на которых нужно включить OSPF. Имя переменной - ospf_intf. На месте этой переменной ожидается список
      словарей с такими ключами:
        – name - имя интерфейса, вида Fa0/1, Vlan10, Gi0/0
        – ip - IP-адрес интерфейса, вида 10.0.1.1
        – area - номер зоны
        – passive - является ли интерфейс пассивным. Допустимые значения: True или False
Для всех интерфейсов в списке ospf_intf, надо сгенерировать строки:
    network x.x.x.x 0.0.0.0 area x
Если интерфейс пассивный, для него должна быть добавлена строка:
    passive-interface x
Для интерфейсов, которые не являются пассивными, в режиме конфигурации интерфейса, надо добавить строку:
    ip ospf hello-interval 1
Все команды должны быть в соответствующих режимах.
Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf.yml, с помощью функции
generate_config из задания 1. Не копируйте код функции generate_config.
"""

from exercise01 import generate_config
import yaml


def create_template_ospf(template: str) -> None:
    """
    This function create template for configuration of ospf
    :param template: the path where you want to save the template
    :return: None
    """
    ospf = """
router ospf {{ process }}
 router-id {{ router_id }}
 auto-cost reference-bandwidth {{ref_bw}}
 {% for networks in ospf_intf %}
 network {{networks.ip}} 0 0.0.0.0 area {{networks.area}}
 {% if networks.passive %}
 passive-interface {{networks.name}}
 {% endif %}
 {% endfor %} 
 
{% for interface in ospf_intf if not interface.passive %}
interface {{interface.name}}
 ip ospf hello-interval 1
{% endfor %}
 """
    with open(template, 'w') as f:
        f.write(ospf)


if __name__ == '__main__':
    data_file = "data_files/ospf.yml"
    template_file = "templates/ospf.txt"
    create_template_ospf('templates/ospf.txt')
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
