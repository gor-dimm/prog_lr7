#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list(peoples):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Фамилия и имя",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)

    # Вывести данные о всех людях:
    for idx, people in enumerate(peoples, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                people.get('name', ''),
                people.get('zod', ''),
                people.get('birth', 0)
            )
        )

    print(line)
