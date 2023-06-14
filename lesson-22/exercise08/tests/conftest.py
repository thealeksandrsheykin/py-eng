# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import pytest
import yaml
from netmiko import ConnectHandler


def test_attr_or_method(obj, attr=None, method=None):
    if attr:
        assert getattr(obj, attr, None) is not None, "Атрибут не найден"
    if method:
        assert getattr(obj, method, None) is not None, "Метод не найден"


@pytest.fixture(scope='module')
def first_router_from_devices_yaml():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
    return r1


@pytest.fixture(scope='module')
def r1_test_telnet_connection():
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1_params = devices[0]
    options = {"device_type": "cisco_ios_telnet"}
    r1_params.update(options)
    r1 = ConnectHandler(**r1_params)
    r1.enable()
    yield r1
    r1.disconnect()
