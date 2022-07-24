"""Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов."""

def my_func(x, y, z):
    sums = [x, y, z]
    sums.sort(reverse=True)
    return sum(sums[0:2])

print(my_func(int(input("Enter first argument ")), int(input("Enter second argument ")), int(input("Enter third argument "))))