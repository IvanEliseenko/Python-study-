my_list = [2, 'Ivan', 456, 45.3, [3, 5],{6, 7}, {'name': 'Ivan'},
           False, None, b'Ivan', 1+2j, frozenset(), bytearray(), TypeError]
for el in my_list:
    print(el, type(el))