#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select():
    parts = command.split(' ', maxsplit=2)
    sel = (parts[1])

    count = 0
    for people in peoples:
        if people.get('zod') == sel:
            count = "Знак Зодиака"
            print('{:>4}: {}'.format(count, people.get('zod', ''))
                  )
            print('Фамилия и имя:', peoples.get('name', ''))
            print('Дата рождения:', peoples.get('birth', ''))

    if count == 0:
        print("Люди с данным знаком Зодиака не найдены.")
