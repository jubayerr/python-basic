# exponent function

def raise_to_power(base, power):
    res = 1
    for index in range(power):
        res = res * base
    return res


result = raise_to_power(3, 2)

print(result)
