# есть список со списками(людьми), там цена до города а и до города б.
# Нужно за минимальную стоимость доставить этих людей в города, но при этом в каждом городе должно быть одинаковое кол-во людей
# сложность O(N)



def twoCitySchedCost(costs):
    res=0
    size=len(costs)/2       #  максимальное количество людей в одном городе
    CityA=0                 # количество людей в городе А
    CityB=0                 # количество людей в городе Б
    costs=sorted(costs, key=lambda x:abs(x[0]-x[1]),reverse=True)   # сортируем список по возрастанию разниц между ценами в А и Б

    for i in costs:                     # проходимся по списку
        if CityB<size and i[0]>=i[1]:
            res+=i[1]
            CityB+=1
        elif CityA<size and i[1]>=i[0]:
            res+=i[0]
            CityA+=1
        elif CityA==size:
            res+=i[1]
        elif CityB==size:
            res+=i[0]


    return(res)

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))