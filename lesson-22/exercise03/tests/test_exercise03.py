import sys
import pytest
import exercise03
from pyeng_common_functions import (check_attr_or_method, check_class_exists,check_pytest, stdout_incorrect_warning,
                                    unify_topology_dict)

sys.path.append("..")
check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(exercise03, "Topology")


@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                                                       ('SW1','Eth0/1'): ('R1', 'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = exercise03.Topology(topology_with_dupl_links)
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
    top_with_data = exercise03.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"


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
def test_method_delete_link_created(
    topology_with_dupl_links, normalized_topology_example
):
    """Проверяем, что в объекте Topology есть метод delete_link"""
    norm_top = exercise03.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_link")


@pytest.mark.parametrize('normalized_topology_example', [({('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                                                           ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                                                           ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                           ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                                                           ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                                                           ('R3', 'Eth0/2'): ('R5', 'Eth0/0')})])
def test_method_delete_link(normalized_topology_example, capsys):
    """Проверка работы метода delete_link"""
    norm_top = exercise03.Topology(normalized_topology_example)
    delete_link_result = norm_top.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    assert None == delete_link_result, "Метод delete_link не должен ничего возвращать"

    assert ("R3", "Eth0/0") not in norm_top.topology, "Соединение не было удалено"

    # проверка удаления зеркального линка
    norm_top.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    assert ("R3", "Eth0/2") not in norm_top.topology, "Соединение не было удалено"

    # проверка удаления несуществующего линка
    norm_top.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))
    out, err = capsys.readouterr()
    link_msg = "Такого соединения нет"
    assert (
        link_msg in out
    ), "При удалении несуществующего соединения, не было выведено сообщение 'Такого соединения нет'"