# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
В этом задании нужно:
    • взять содержимое нескольких файлов с выводом команды sh version
    • распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
    • записать полученную информацию в файл в CSV формате
Для выполнения задания нужно создать две функции. Функция parse_sh_version:
    • ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
    • обрабатывает вывод, с помощью регулярных выражений
    • возвращает кортеж из трёх элементов:
        – ios - в формате «12.4(5)T»
        – image - в формате «flash:c2800-advipservicesk9-mz.124-5.T.bin»
        – uptime - в формате «5 days, 3 hours, 3 minutes»
У функции write_inventory_to_csv должно быть два параметра:
    • data_filenames - ожидает как аргумент список имен файлов с выводом sh version
    • csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация
     в формате CSV
Функция write_inventory_to_csv записывает содержимое в файл, в формате CSV и ничего невозвращает.
Функция write_inventory_to_csv должна делать следующее:
    • обработать информацию из каждого файла с выводом sh version:
        – sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
    • с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
    • из имени файла нужно получить имя хоста
    • после этого вся информация должна быть записана в CSV файл
В файле routers_inventory.csv должны быть такие столбцы: hostname, ios, image, uptime
В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers. Вы можете раскомментировать
строку print(sh_version_files), чтобы посмотреть содержимое списка. Кроме того, создан список заголовков (headers),
который должен быть записан в CSV.

    import glob
    sh_version_files = glob.glob("sh_vers*")
    #print(sh_version_files)
    headers = ["hostname", "ios", "image", "uptime"]
'''
import re
import csv
import glob

def parse_sh_version(sh_version):
    '''
    Функция обрабатывает вывод, с помощью регулярных выражений
    :param sh_version: вывод команды sh version одной строкой (не имя файла)
    :return: кортеж из трёх элементов:
                    – ios    - в формате «12.4(5)T»
                    – image  - в формате «flash:c2800-advipservicesk9-mz.124-5.T.bin»
                    – uptime - в формате «5 days, 3 hours, 3 minutes»
    '''
    regex = (
        'Cisco IOS .*? Version (?P<ios>\S+), .*'
        'uptime is (?P<uptime>[\w, ]+).*'
        'image file is "(?P<image>\S+)".*')
    match = re.search(regex,sh_version,re.DOTALL)
    if match:
        return match.group('ios','image','uptime')



def write_inventory_to_csv(data_filenames,csv_filename):
    '''
    Функция записывает содержимое в файл.
    :param data_filenames: список имен файлов с выводом sh version
    :param csv_filename: имя файла, в который будет записана информация в формате CSV
    :return: ничего не возвращает
    '''
    headers = ["hostname", "ios", "image", "uptime"]
    with open (csv_filename, 'w+', newline='') as file_out:
        writer = csv.writer(file_out, delimiter=';')
        writer.writerow(headers)
        for file in data_filenames:
            hostname = (re.search(r'\S+_(\S+).txt',file)).group(1)
            with open(file,'r') as file_in:
                data = list(parse_sh_version(file_in.read()))
                writer.writerow([hostname]+data)


if __name__ == '__main__':
    sh_version_files = glob.glob("sh_vers*")
    write_inventory_to_csv(sh_version_files,'routers_inventory.csv')

