"""Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу."""

res = []
while True:
    args = input("Add numbers (enter or add 'Q' for finish): ")
    if args == 'Q':
        break
    else:
        def str_sum(args):
            while True:
                if args.endswith('Q'):
                    z = args.replace('Q', '0')
                    x = [int(z) for z in z.split()]
                    res.extend(x)
                    return sum(res)
                else:
                    x = [int(x) for x in args.split()]
                    res.extend(x)
                    return sum(res)
    print(str_sum(args))
    if args.endswith('Q'):
        break
