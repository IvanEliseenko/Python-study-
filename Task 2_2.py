lst = input("Enter numbers: ").split()
for i in range(1, len(lst), 2):
    lst.insert(i-1, lst.pop(i))
print(lst)
