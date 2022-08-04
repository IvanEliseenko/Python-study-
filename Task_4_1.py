"""Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами."""

from sys import argv

scrt_name, work_hours, salary, bonus = argv
work_hours = int(work_hours)
salary = int(salary)
bonus = int(bonus)
payment = work_hours * salary + bonus
print("Script name:", scrt_name)
print("Working hours:", work_hours)
print("Salary: ", salary)
print("Bonus: ", bonus)
print("Payment: ", payment)
# Done
