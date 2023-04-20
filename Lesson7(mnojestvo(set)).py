cities = ['Moscow','Las Vegas','Paris','Moscow']
print(type(cities))
print(cities)

print('убираем дубли с помощью set')
cities = set(cities)
print(cities)
print(type(cities))

print('можно сразу задать множество и даже с дублями так как функция их уберет')
cities = {'Moscow','Las Vegas','Paris','Moscow'}
print(cities)

print('можно добавить что-то во множество')
cities.add('Turkey')
print(cities)

print('можно удалить элемент из множества')
cities.remove('Moscow')
print(cities)

print('узнать длинну или количество элементов')
print(len(cities))

print('узнать есть ли что-то во множестве')
print("Paris" in cities)

print('так же можно циклом for перебрать список')
for city in cities:
    print(city)

print('рассмотрим практический пример ------------------------------------------------------------------------')

#семейная пара собирается в отпуск
#каждый из супругов собирает в поездку вещи
#макс взял эти вещи
max_things = {'Телефон','Бритва','Рубашка','Шорты'}
#кейт взяла эти вещи
kate_things = {'Телефон','Шорты','Зонтик','Помада'}
#Какие вещи взяли супруги ?
print(max_things | kate_things)
#найденные вещи повторяются ?
print(max_things & kate_things)
#какие вещи взял макс но не взяла кейт?
print(max_things - kate_things)
#какие вещи взяла кейт но не взял макс ?
print(kate_things - max_things)