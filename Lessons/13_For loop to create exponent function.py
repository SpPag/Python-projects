
def raise_what_to_what_power(number, power):
    multiplication_term = 1
    for chicken in range(power):
        multiplication_term = multiplication_term * number
    return multiplication_term


print(raise_what_to_what_power(3, 2))
