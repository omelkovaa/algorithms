# Все достаточно понятно,  выполняем действия с while,
# пока не найдется один победитель, будет выполнятся цикл
# Сложность равна O(N)

def number(n):
    matches = 0 # количество сыгранных матчей
    while n != 1: # выявления победителя
        if n % 2 == 0: # проверка четного числа
            matches += n // 2 # занесли матчи в счетчик
            n = n // 2 # перезапись количества команд
        else:
            matches += (n-1) // 2 # количество матчей при нечетном количестве команд
            n = ((n - 1) // 2) + 1 # перезапись количества команд
    return matches # возвращаю счетчик
