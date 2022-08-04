"""Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится."""

from itertools import count
from itertools import cycle
for el in count(int(input("Enter number before 20: "))):
    c = 0
    for i in cycle(["A", 12, False]):
        if c > 2:
            break
        else:
            c += 1
            print(i)
    if el > 20:
        break
    else:
        print(el)
# Done