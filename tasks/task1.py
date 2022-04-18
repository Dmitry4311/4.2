#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""Поле first — дробное число; поле second — целое число, показатель степени. Реализовать
метод power() — возведение числа first в степень second. Метод должен правильно
работать при любых допустимых значениях first и second. Максимально задействовать имеющиеся в Python
средства перегрузки операторов"""


class Number:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if self.first == 0:
            raise ValueError

    def __pow__(self, other):
        a = self.first + self.second
        b = other.first + other.second
        return a ** b


if __name__ == "__main__":
    num1 = Number(1.5, 0)
    num2 = Number(2, 0)
    print(f"Число возведенное в степень равняется: {num1 ** num2}")