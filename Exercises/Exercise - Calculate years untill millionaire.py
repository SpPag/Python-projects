money = 155
interest_rate = 0.03
years_passed = 0
while money < 1000000:
    years_passed += 1
    money = money + money * interest_rate
print("Money accumulated: ", money)
print("Years to become a millionaire: ", years_passed)
