#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
