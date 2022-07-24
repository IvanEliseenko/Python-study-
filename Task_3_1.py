"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль"""


def dev_func(n_1, n_2):
    try:
        dev = n_1 / n_2
        print(f"Result: {dev}")
    except ZeroDivisionError:
        print("Error: Division by 0")


dev_func(float(input("Add devidend: ")), float(input("Add devider: ")))
