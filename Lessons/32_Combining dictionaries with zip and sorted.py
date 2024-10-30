stocks = {
    "a": 2,
    "b": 5,
    "c": 14,
    "d": 21,
    "f": 6,
    "e": 1
}

print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))
