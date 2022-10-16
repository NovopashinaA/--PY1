salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # (1+0.03) рост цен для удобства

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for month in range(1, months+1):
    need_money += spend
    need_money -= salary
    spend *= increase
print(round(need_money))
