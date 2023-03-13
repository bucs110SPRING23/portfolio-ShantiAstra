def multiplication(first, second):
    total = 0
    for _ in range(second):
        total += first
    return total
def raise_to_exp(base, exponant):
    total = base
    for _ in range(exponant-1):
        total = total*base
    return total
def square(num):
    return multiplication(num,num)
print(multiplication(5,3))
print(raise_to_exp(2,5))
print(square(6))