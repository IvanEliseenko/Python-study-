sec_value = float(input("Enter time in sec.: "))

hour_value = sec_value // 3600
min_value = (sec_value % 3600) // 60
sec_reside = sec_value - (min_value * 60) - (hour_value * 3600)

print(f"{int(hour_value)}:{int(min_value)}:{int(sec_reside)}")
