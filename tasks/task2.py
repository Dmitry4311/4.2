#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
Создать класс BitString для работы с битовыми строками не более чем из 100 бит. Битовая
строка должна быть представлена списком типа int, каждый элемент которого принимает
значение 0 или 1. Реальный размер списка задается как аргумент конструктора
инициализации. Должны быть реализованы все традиционные операции для работы с
битовыми строками: and, or, xor, not. Реализовать сдвиг влево и сдвиг вправо на заданное
количество битов.
"""


class BitString:
    
    def __init__(self, x):
        # Инициализация
        self.size = x
        self.x = [0] * self.size

    def set(self, x):
        # Установка значения
        self.x = list(map(int, f'{x:b}'.rjust(self.size, '0')))

    def __invert__(self):
        # Оператор not (~)
        self.x = [int(not i) for i in self.x]
        return self

    def __or__(self, other):
        # Оператор or (|)
        x = [a | b for a, b in zip(self.x, other.x)]
        return ''.join(map(str, x))

    def __xor__(self, other):
        # Оператор xor (^)
        x = [a ^ b for a, b in zip(self.x, other.x)]
        return ''.join(map(str, x))

    def __and__(self, other):
        # Оператор and (&)
        x = [a & b for a, b in zip(other.x, self.x)]
        return ''.join(map(str, x))

    def __lshift__(self, x):
        # Оператор сдвиг влево (<<)
        del (self.x[0:x])
        self.x += [0] * x
        return self

    def __rshift__(self, x):
        # Оператор сдвиг вправо (>>)
        del (self.x[len(self.x) - x:])
        self.x = [0] * x + self.x
        return self

    def __str__(self):
        # Вывод результата в консоль
        return ''.join(map(str, self.x))


if __name__ == "__main__":
    x = BitString(8)  # Размер списка 1 - 8 бит
    y = BitString(8)  # Размер списка 2 - 8 бит

    x.set(60)  # Первая цифра 00111100
    print(x)
    y.set(37)  # Вторая цифра 00100101
    print(y)

    print(f'{x} and {y} = {x & y}')
    print(f'{x} or {y} = {x | y}')
    print(f'{x} xor {y} = {x ^ y}')
    print(f'{x} not = {~x}')
    print(f'{y} >> 1 = {y >> 1}')
    print(f'{x} << 2 = {x << 2}')
