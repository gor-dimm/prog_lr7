#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата рождения. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи
# должны быть упорядочены по датам рождения; вывод на экран информации о людях, родившихся под знаком, название
# которого введено с клавиатуры; если таких нет, выдать на дисплей соответствующее сообщение.


import sys
from folder import add, list, help, select

if __name__ == '__main__':
    # Список .
    peoples = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>>>>>",).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
           break

        elif command == 'add':
            add.add(peoples)

        elif command == 'list':
             list.list(peoples)

        elif command.startswith('select '):
             select.select(peoples)

        elif command == 'help':
            help.help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
