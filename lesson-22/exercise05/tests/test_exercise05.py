# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import pytest
import warnings
import exercise05
from pyeng_common_functions import (check_class_exists, check_attr_or_method, stdout_incorrect_warning,)

sys.path.append("..")


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(exercise05, "Topology")


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
    top_with_data = exercise05.Topology(topology_with_dupl_links)
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
    top_with_data = exercise05.Topology(topology_with_dupl_links)
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
def test_method_add_link_created(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть метод add_link"""
    norm_top = exercise05.Topology(topology_with_dupl_links)
    check_attr_or_method(norm_top, method="add_link")


@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                                                       ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_method_add_link(topology_with_dupl_links, capsys):
    """Проверка работы метода add_link"""
    norm_top = exercise05.Topology(topology_with_dupl_links)

    add_link_result = norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert add_link_result == None, "Метод add_link не должен ничего возвращать"

    assert (
        "R1",
        "Eth0/4",
    ) in norm_top.topology, "После добавления соединения через метод add_link, оно должно существовать в топологии"
    assert (
        len(norm_top.topology) == 7
    ), "После добавления соединения количество соединений должно быть равно 7"

    # проверка добавления существующего линка
    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    out, err = capsys.readouterr()
    link_msg = "Такое соединение существует"
    assert (
        link_msg in out
    ), "При добавлении существующего соединения, не было выведено сообщение 'Такое соединение существует'"

    # проверка добавления линка с существующим портом
    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    out, err = capsys.readouterr()
    port_msg = "Cоединение с одним из портов существует"
    assert (
        port_msg in out
    ), "При добавлении соединения с существующим портом, не было выведено сообщение 'Cоединение с одним из портов существует'"