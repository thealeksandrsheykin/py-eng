import sys
import pytest
import exercise02
from pyeng_common_functions import (check_attr_or_method, check_class_exists, check_pytest, unify_topology_dict)

sys.path.append("..")

check_pytest(__loader__, __file__)


def test_class_created():
    """
    Проверка, что класс создан
    """
    check_class_exists(exercise02, "Topology")

@pytest.mark.parametrize('topology_with_dupl_links', [{('R1', 'Eth0/0'): ('SW1', 'Eth0/1' ),
                                                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2' ),
                                                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3' ),
                                                       ('R3', 'Eth0/1'): ('R4', 'Eth0/0'  ),
                                                       ('R3', 'Eth0/2'): ('R5', 'Eth0/0'  ),
                                                       ('SW1','Eth0/1'): ('R1', 'Eth0/0'  ),
                                                       ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}])
def test_attr_topology(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть атрибут topology"""
    top_with_data = exercise02.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")

@pytest.mark.parametrize('topology_with_dupl_links', [{('R1',  'Eth0/0'): ('SW1', 'Eth0/1' ),
                                                       ('R2',  'Eth0/0'): ('SW1', 'Eth0/2' ),
                                                       ('R2',  'Eth0/1'): ('SW2', 'Eth0/11'),
                                                       ('R3',  'Eth0/0'): ('SW1', 'Eth0/3' ),
                                                       ('R3',  'Eth0/1'): ('R4',  'Eth0/0'),
                                                       ('R3',  'Eth0/2'): ('R5',  'Eth0/0'),
                                                       ('SW1', 'Eth0/1'): ('R1',  'Eth0/0'),
                                                       ('SW1', 'Eth0/2'): ('R2',  'Eth0/0'),
                                                       ('SW1', 'Eth0/3'): ('R3',  'Eth0/0')}])
def test_method_normalize(topology_with_dupl_links):
    """Проверяем, что в объекте Topology есть метод _normalize"""
    top_with_data = exercise02.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, method="_normalize")


@pytest.mark.parametrize('topology_with_dupl_links,'
                         ' normalized_topology_example', [({('R1',  'Eth0/0'): ('SW1', 'Eth0/1'),
                                                            ('R2',  'Eth0/0'): ('SW1', 'Eth0/2'),
                                                            ('R2',  'Eth0/1'): ('SW2', 'Eth0/11'),
                                                            ('R3',  'Eth0/0'): ('SW1', 'Eth0/3'),
                                                            ('R3',  'Eth0/1'): ('R4', 'Eth0/0'),
                                                            ('R3',  'Eth0/2'): ('R5', 'Eth0/0'),
                                                            ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                                                            ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                                                            ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')},
                                                           {('R1',  'Eth0/0'): ('SW1', 'Eth0/1'),
                                                            ('R2',  'Eth0/0'): ('SW1', 'Eth0/2'),
                                                            ('R2',  'Eth0/1'): ('SW2', 'Eth0/11'),
                                                            ('R3',  'Eth0/0'): ('SW1', 'Eth0/3'),
                                                            ('R3',  'Eth0/1'): ('R4',  'Eth0/0'),
                                                            ('R3',  'Eth0/2'): ('R5', 'Eth0/0')})])
def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = exercise02.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"По заданию в переменной topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"
    assert (
        correct_topology == return_topology
    ), "После создания экземпляра, в переменной topology должна находиться топология без дублей"