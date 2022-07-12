x = float(input("Add 'x' value: "))
y = float(input("Add 'y' value: "))
st_act = input("Add type of calculation(+, -, *, :): ")

if st_act == str("+"):
    print(x + y)
elif st_act == str("-"):
    print(x - y)
elif st_act == str("*"):
    print(x * y)
elif st_act == str(":") and y != 0:
    print(x / y)
else:
    print("UNIVERSAL COLLAPSE")
