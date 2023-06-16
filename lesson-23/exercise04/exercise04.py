# -*- coding: utf-8 -*-
# !/usr/bin/env python3

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        result = dict()
        for key, value in topology_dict.items():
            if not result.get(value):
                result[key] = value
        return result

    def delete_link(self, local, remote):
        if self.topology.get(local) == remote:
            del self.topology[local]
        elif self.topology.get(remote) == local:
            del self.topology[remote]
        else:
            print(f'Такого соединения нет!')

    def delete_node(self, device):
        length = len(self.topology)
        topology_list = list(self.topology.items())
        for local, remote in topology_list:
            if device in local or device in remote:
                del self.topology[local]
        if len(self.topology) == length:
            print(f'Такого устройства нет!')

    def add_link(self, local, remote):
        data = set(self.topology.keys()) | set(self.topology.values())
        if self.topology.get(local) == remote or self.topology.get(remote) == local:
            print(f'Такое соединение существует!')
        elif local in data or remote in data:
            print(f'Cоединение с одним из портов существует')
        else:
            self.topology[local] = remote

    def __add__(self, other):
        return Topology(self.topology | other.topology)


if __name__ == '__main__':
    topology_example1 = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                         ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                         ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                         ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                         ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                         ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                         ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                         ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                         ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    t1 = Topology(topology_example1)
    # print(t1.topology)
    topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                         ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    t2 = Topology(topology_example2)
    # print(t2.topology)
    t3 = t1 + t2
    print(t3.topology)
