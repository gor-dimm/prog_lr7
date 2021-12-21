#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(peoples):
    name = input("Фамилия и имя? ")
    zod = input("Знак Зодиака? ")
    birth = input("Дата рождения? ")

    # Создать словарь:
    people = {
        'name': name,
        'zod': zod,
        'birth': birth,
    }

    # Добавить словарь в список:
    peoples.append(people)
    # Отсортировать список.
    peoples.sort(key=lambda item: item.get('zod', ''))
