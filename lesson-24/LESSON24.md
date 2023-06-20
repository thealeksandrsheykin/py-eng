# LESSON 24

## Задание №1

Создать класс CiscoSSH, который наследует класс BaseSSH из файла base_connect_class.py.  Создать метод __init__ в классе
CiscoSSH таким образом, чтобы после подключения по SSH выполнялся переход в режим enable. Для этого в методе __init__ 
должен сначала вызываться метод __init__ класса ConnectSSH, а затем выполняться переход в режим enable.

```python
In [2]: from exercise01 import CiscoSSH
In [3]: r1 = CiscoSSH(**device_params)
In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface        IP-Address      OK?   Method Status Protocol
         Ethernet0/0      192.168.100.1   YES    NVRAM   up      up
         Ethernet0/1      192.168.200.1   YES    NVRAM   up      up 
         Ethernet0/2      190.16.200.1    YES    NVRAM   up      up 
         Ethernet0/3      192.168.230.1   YES    NVRAM   up      up 
         Ethernet0/3.100  10.100.0.1      YES    NVRAM   up      up 
         Ethernet0/3.200  10.200.0.1      YES    NVRAM   up      up 
         Ethernet0/3.300  10.30.0.1       YES    NVRAM   up      up'

```
