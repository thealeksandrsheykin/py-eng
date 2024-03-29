# LESSON 24

## Задание №1

Создать класс CiscoSSH, который наследует класс BaseSSH из файла base_connect_class.py.  Создать метод `__init__` в классе
CiscoSSH таким образом, чтобы после подключения по SSH выполнялся переход в режим enable. Для этого в методе `__init__` 
должен сначала вызываться метод `__init__` класса ConnectSSH, а затем выполняться переход в режим enable.

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

## Задание №2

Скопировать и дополнить класс CiscoSSH из задания №1.Перед подключением по SSH необходимо проверить если ли в словаре с 
параметрами подключения такие параметры: username, password, secret. Если какого-то параметра нет, запросить значение у 
пользователя, а затем выполнять подключение. Если все параметры есть, выполнить подключение.
```python
In [1]: from exercise02 import CiscoSSH
In [2]: device_params = {
            'device_type': 'cisco_ios',
            'host': '192.168.100.1'}
In [3]: r1 = CiscoSSH(**device_params)
        Введите имя пользователя: admin
        Введите пароль: cisco
        Введите пароль для режима enable: cisco
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

## Задание №3

Создать класс `MyNetmiko`, который наследует класс `CiscoIosSSH` из netmiko. Переписать метод `__init__` в классе `MyNetmiko` 
таким образом, чтобы после подключения по SSH выполнялся переход в режим enable. Для этого в методе `__init__` должен 
сначала вызываться метод `__init__` класса `CiscoIosBase`, а затем выполнялся переход в режим enable. Проверить, что в 
классе `MyNetmiko` доступны методы `send_command` и `send_config_set` (они наследуются автоматически, это только для 
проверки).

```python
In [2]: from exercise03 import MyNetmiko
In [3]: r1 = MyNetmiko(**device_params)
In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface        IP-Address      OK?   Method Status Protocol
         Ethernet0/0      192.168.100.1   YES    NVRAM   up      up
         Ethernet0/1      192.168.200.1   YES    NVRAM   up      up 
         Ethernet0/2      190.16.200.1    YES    NVRAM   up      up 
         Ethernet0/3      192.168.230.1   YES    NVRAM   up      up 
         Ethernet0/3.100  10.100.0.1      YES    NVRAM   up      up 
         Ethernet0/3.200  10.200.0.1      YES    NVRAM   up      up 
         Ethernet0/3.300  10.30.0.1       YES    NVRAM   up      up'
```

Импорт класса CiscoIosSSH:
```python
from netmiko.cisco.cisco_ios import CiscoIosSSH
device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
```

## Задание №4

Скопировать и дополнить класс `MyNetmiko` из задания №3. Добавить метод `_check_error_in_command`, который выполняет проверку
на такие ошибки:
1. Invalid input detected
2. Incomplete command
3. Ambiguous command

Метод ожидает как аргумент команду и вывод команды. Если в выводе не обнаружена ошибка, метод ничего не возвращает. Если
в выводе найдена ошибка, метод генерирует исключение `ErrorInCommand` с сообщением о том какая ошибка была обнаружена, на
каком устройстве и в какой команде. Переписать метод `send_command` netmiko, добавив в него проверку на ошибки.

```python
In [2]: from exercise04 import MyNetmiko
In [3]: r1 = MyNetmiko(**device_params)
In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface        IP-Address      OK?   Method Status Protocol
         Ethernet0/0      192.168.100.1   YES    NVRAM   up      up
         Ethernet0/1      192.168.200.1   YES    NVRAM   up      up 
         Ethernet0/2      190.16.200.1    YES    NVRAM   up      up 
         Ethernet0/3      192.168.230.1   YES    NVRAM   up      up 
         Ethernet0/3.100  10.100.0.1      YES    NVRAM   up      up 
         Ethernet0/3.200  10.200.0.1      YES    NVRAM   up      up 
         Ethernet0/3.300  10.30.0.1       YES    NVRAM   up      up'

In [5]: r1.send_command('sh ip br')
---------------------------------------------------------------------------
ErrorInCommand Traceback (most recent call last) <ipython-input-2-1c60b31812fd> in <module>() 1 r1.send_command('sh ip br')
ErrorInCommand: При выполнении команды "sh ip br" на устройстве 192.168.100.1 возникла ошибка "Invalid input detected at '^' marker."
```

Исключение ErrorInCommand:

```python
class ErrorInCommand(Exception):
"""
    Исключение генерируется, если при выполнении команды на оборудовании, возникла ошибка.
"""
```

## Задание №5

Скопировать класс `MyNetmiko` из задания №4. Дополнить функционал метода `send_config_set` netmiko и добавить в него проверку
на ошибки с помощью метода `_check_error_in_command`. Метод `send_config_set` должен отправлять команды по одной и проверять
каждую на ошибки. Если при выполнении команд не обнаружены ошибки, метод `send_config_set` возвращает вывод команд.

```python
In [2]: from exercise05 import MyNetmiko
In [3]: r1 = MyNetmiko(**device_params)
In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand Traceback (most recent call last)<ipython-input-2-8e491f78b235> in <module>() 1 r1.send_config_set('lo')
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла␣ошибка "Incomplete command."
```

## Задание №6

Скопировать класс MyNetmiko из задания 24.2b. Проверить, что метод send_command кроме
команду, принимает еще и дополнительные аргументы, например, strip_command.
Если возникает ошибка, переделать метод таким образом, чтобы он принимал любые аргументы, которые поддерживает netmiko.
```python
In [2]: from exercise06 import MyNetmiko
In [3]: r1 = MyNetmiko(**device_params)
In [4]: r1.send_command('sh ip int br', strip_command=False)
Out[4]: 'sh ip int br
         Interface        IP-Address      OK?   Method Status Protocol
         Ethernet0/0      192.168.100.1   YES    NVRAM   up      up
         Ethernet0/1      192.168.200.1   YES    NVRAM   up      up 
         Ethernet0/2      190.16.200.1    YES    NVRAM   up      up 
         Ethernet0/3      192.168.230.1   YES    NVRAM   up      up 
         Ethernet0/3.100  10.100.0.1      YES    NVRAM   up      up 
         Ethernet0/3.200  10.200.0.1      YES    NVRAM   up      up 
         Ethernet0/3.300  10.30.0.1       YES    NVRAM   up      up'

In [5]: r1.send_command('sh ip int br', strip_command=True)
Out[5]: 'Interface        IP-Address      OK?   Method Status Protocol
         Ethernet0/0      192.168.100.1   YES    NVRAM   up      up
         Ethernet0/1      192.168.200.1   YES    NVRAM   up      up 
         Ethernet0/2      190.16.200.1    YES    NVRAM   up      up 
         Ethernet0/3      192.168.230.1   YES    NVRAM   up      up 
         Ethernet0/3.100  10.100.0.1      YES    NVRAM   up      up 
         Ethernet0/3.200  10.200.0.1      YES    NVRAM   up      up 
         Ethernet0/3.300  10.30.0.1       YES    NVRAM   up      up'
```

## Задача №7

Скопировать класс `MyNetmiko` из задания №6 или задания №5. Добавить параметр `ignore_errors` в метод `send_config_set`.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен работать точно так же как метод
`send_config_set` в netmiko. Если значение ложное, ошибки должны проверяться. По умолчанию ошибки должны игнорироваться.

```python
In [2]: from exercise07 import MyNetmiko
In [3]: r1 = MyNetmiko(**device_params)
In [6]: r1.send_config_set('lo')
Out[6]: config term
        Enter configuration commands, one per line. End with CNTL/Z.
        R1(config)#lo
        % Incomplete command.

        R1(config)#end
        R1#
In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term
         Enter configuration commands, one per line. End with CNTL/Z.
         R1(config)#lo
         % Incomplete command.

         R1(config)#end
         R1#
         
In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand Traceback (most recent call last) <ipython-input-8-704f2e8d1886> in <module>() 1 r1.send_config_set('lo', ignore_errors=False)
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла␣ошибка "Incomplete command."
```