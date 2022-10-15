salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0

current_spend = spend
for i in range (1, months + 1):
    i = current_spend - salary
    current_spend = current_spend * (1 + increase)
    need_money += i

print(round (need_money))
