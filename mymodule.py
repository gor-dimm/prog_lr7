#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def zamena(a, b):
    def change(str):
        str = str.replace(a, b)
        ans = ""
        for i in range(0, len(str)):
            if str[i] != str[i - 1]:
                ans += str[i]
        return ans
    return change
