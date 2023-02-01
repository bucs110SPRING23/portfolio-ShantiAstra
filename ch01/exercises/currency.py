exchange_rate = float(input("How many US dollars is one Euro worth?"))
amount = float(input("How many Euros would you like to exchange today?"))
total = amount * exchange_rate
result = total - 3.00
print("You recieve", result, "US dollars")