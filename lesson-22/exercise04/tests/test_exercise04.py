# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import pytest
import exercise04
from pyeng_common_functions import (check_class_exists, check_attr_or_method, stdout_incorrect_warning)

sys.path.append("..")

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(exercise04, "Topology")


@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                                                       ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = exercise04.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")

@pytest.mark.parametrize('topology_with_dupl_links, '
                         'normalized_topology_example', [({('R1',  'Eth0/0'): ('SW1', 'Eth0/1'),
                                                           ('R2',  'Eth0/0'): ('SW1', 'Eth0/2'),
                                                           ('R2',  'Eth0/1'): ('SW2', 'Eth0/11'),
                                                           ('R3',  'Eth0/0'): ('SW1', 'Eth0/3'),
                                                           ('R3',  'Eth0/1'): ('R4', 'Eth0/0'),
                                                           ('R3',  'Eth0/2'): ('R5', 'Eth0/0'),
                                                           ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                           ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                           ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')},
                                                          {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                           ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                           ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                           ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                           ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                           ('R3', 'Eth0/2'): ('R5', 'Eth0/0')})])
def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = exercise04.Topology(topology_with_dupl_links)
    assert (
            type(top_with_data.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                                                       ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_method_delete_node_created(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть метод delete_node"""
    norm_top = exercise04.Topology(topology_with_dupl_links)
    check_attr_or_method(norm_top, method="delete_node")


@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                                                       ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_method_delete_node(topology_with_dupl_links, capsys):
    """Проверка работы метода delete_node"""
    norm_top = exercise04.Topology(topology_with_dupl_links)

    node = "SW1"
    delete_node_result = norm_top.delete_node(node)
    assert delete_node_result == None, "Метод delete_node не должен ничего возвращать"

    ports_with_node = [
        src for src, dst in norm_top.topology.items() if node in src or node in dst
    ]
    assert len(ports_with_node) == 0, "Соединения с хостом SW1 не были удалены"
    assert (
            len(norm_top.topology) == 3
    ), "В топологии должны остаться только три соединения"

    # проверка удаления несуществующего устройства
    norm_top.delete_node(node)
    out, err = capsys.readouterr()
    node_msg = "Такого устройства нет"
    assert (
            node_msg in out
    ), "При удалении несуществующего устройства, не было выведено сообщение 'Такого устройства нет'"
