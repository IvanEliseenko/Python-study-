seasons = dict(Winter=[1, 12, 2], Spring=[3, 5, 4], Summer=[6, 7, 8], Autumn=[9, 10, 11])
m_num = str(input("Enter number of the month: "))
if m_num in str(list(seasons.values())):
    for i in seasons.items():
        if m_num in str(i[1]):
                print(i[0])