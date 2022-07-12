gain = float(input("Enter gain: "))
loss = float(input("Enter loss: "))
if gain > loss:
    print(f"Your gain is {gain - loss}. Congratulations!")
elif gain <= loss:
    print(f"Yor loss is {loss - gain}. Try harder!")
if gain > loss:
    profit = float(input("Enter profit: "))
    empl = int(input("Enter employees number: "))
    if profit > gain:
        print("Error. Profit invalid.")
    else:
        profitability = profit / gain * 100
        empl_prof = profit / empl
        print (f"Your profitability is {profitability}%. It is {empl_prof} for each employee.")
else:
    print("DUMB")
