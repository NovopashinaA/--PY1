money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05 # 1+0.5 для удобства

month = 0

while money_capital >= spend - salary:
    money_capital = money_capital - spend + salary
    spend *= increase
    month += 1
print(month)
