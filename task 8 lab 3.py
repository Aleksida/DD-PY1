money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
ostatok = salary - spend
while money_capital + ostatok >= spend:
    spend = spend * (1 + increase)
    money_capital += ostatok
    month += 1

print(month)
