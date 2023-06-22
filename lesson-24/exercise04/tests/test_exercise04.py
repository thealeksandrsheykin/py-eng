# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import pytest
import exercise04
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyeng_common_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(exercise04, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = exercise04.MyNetmiko(**first_router_from_devices_yaml)
    r1.disconnect()
    assert isinstance(r1, CiscoIosSSH), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(r1, method="send_command")
    check_attr_or_method(r1, method="_check_error_in_command")


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "sh ip br"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_errors(first_router_from_devices_yaml, command, error):
    r1 = exercise04.MyNetmiko(**first_router_from_devices_yaml)
    with pytest.raises(exercise04.ErrorInCommand) as excinfo:
        return_value = r1.send_command(command)
        r1.disconnect()
    assert error in str(
        excinfo
    ), "Метод send_config_commands должен генерировать исключение, когда команда выполнена с ошибкой"