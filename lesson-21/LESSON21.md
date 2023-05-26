# LESSON 21

## Задание №1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)
	
Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.


```python
from netmiko import ConnectHandler
# вызов функции должен выглядеть так
if __name__ == "__main__":
	r1_params = {
		"device_type": "cisco_ios",
		"host": "192.168.100.1",
		"username": "cisco",
		"password": "cisco",
		"secret": "cisco",
	}
	with ConnectHandler(**r1_params) as r1:
		r1.enable()
		output = r1.send_command("sh ip int br")
	result = parse_command_output("templates/sh_ip_int_br.template", output)
	print(result)
```

## Задание №2

Создать функцию parse_output_to_dict.
Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

## Задание №3

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding и записать его в файл templates/sh_ip_dhcp_snooping.template
Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.
Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 1.

## Задание №4

Создать функцию parse_command_dynamic.
Параметры функции:
1. command_output - вывод команды (строка)
2. attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
	- "Command": команда
	- "Vendor": вендор
3. index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
4. templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 2):
1. ключи - имена переменных в шаблоне TextFSM
2. значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.

## Задание №5

Создать функцию send_and_parse_show_command. Параметры функции:
1. device_dict - словарь с параметрами подключения к одному устройству
2. command - команда, которую надо выполнить
3. templates_path - путь к каталогу с шаблонами TextFSM
4. index - имя индекс файла, значение по умолчанию «index»
Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.
Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 2):
- [x] ключи - имена переменных в шаблоне TextFSM
- [x] значения - части вывода, которые соответствуют переменным
Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.

## Задание №6

Создать функцию send_and_parse_command_parallel.
Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 5.
Параметры функции send_and_parse_command_parallel:
1. devices - список словарей с параметрами подключения к устройствам
2. command - команда
3. templates_path - путь к каталогу с шаблонами TextFSM
4. limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать словарь:
1. ключи - IP-адрес устройства с которого получен вывод
2. значения - список словарей (вывод который возвращает функция send_and_parse_show_command)

Пример словаря:
```json
{
	'192.168.100.1': 
		[
		 {'address': '192.168.100.1',
		  'intf': 'Ethernet0/0',
		  'protocol': 'up',
		  'status': 'up'},
    	 {'address': '192.168.200.1',
		  'intf': 'Ethernet0/1',
		  'protocol': 'up',
		  'status': 'up'}
		],
	'192.168.100.2':  
	    [
		 {'address': '192.168.100.2',
		  'intf': 'Ethernet0/0',
		  'protocol': 'up',
		  'status': 'up'},
		 {'address': '10.100.23.2',
		  'intf': 'Ethernet0/1',
		  'protocol': 'up',
		  'status': 'up'}
		]
}
```

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml