a = float(input("Enter first day result (km): "))
b = float(input("Enter objective result (km): "))
d = 0
if a < 0 or b < 0 or b < a:
    print("Are you kidding me?")
elif a > 0 or b > 0 or b > a:
    while a <= b:
        a = a + (a * 0.1)
        d = d + 1
else:
    print(f"Day {d}.")
