print("50", 10*5)
print("100", 10**2)
print("1.5", 15/10)
print("1", 15//10)
print("-1", -15//10)
# integer division apparently rounds down instead of just truncating
print("5", 15%10)
print("10", 10%15)
print("0", 10%10)
print("0", 0%10)
print("0.666666666", 10/15)
#technically this is incorrect since it would be 2/3 and the decimal would need to repeat to infinity
#This ends up with 16 decimal points and then cuts off