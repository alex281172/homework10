
def askinq(messadge, day):
    year_day = int(input(messadge))
    while year_day != day:
        print("Не верно")
        year = input(messadge)


askinq('Ввведите год рождения А.С.Пушкина: ', 1799)
askinq('В какой день июня родился А.С.Пушкина?: ', 6)
print('Верно!')



