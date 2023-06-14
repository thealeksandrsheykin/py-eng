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


if __name__ == '__main__':
    topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    top = Topology(topology_example)
    print(top.topology)
    top.delete_link(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
    print(top.topology)
    top.delete_link(('SW1', 'Eth0/3'), ('R3', 'Eth0/0'))
    print(top.topology)
    top.delete_link(('SW9', 'Eth0/3'), ('R6', 'Eth0/0'))
