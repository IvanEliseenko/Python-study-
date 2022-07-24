"""Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой."""


def user_data(*args):
    x = list(args)
    z = " ".join(x)
    return z


print(user_data(
    str(input("Enter your name: ")).capitalize(),
    str(input("Enter your surname: ")).capitalize(),
    input("Enter your year of birth: "),
    input("Enter current city: ").capitalize(),
    input("Enter your e-mail: "),
    input("Enter your phone number: ")))
