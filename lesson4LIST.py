# объявить пустой список
empty_list = []
#либо можно заполнить лист
friends = ["Max","Leo","Kate"]

# 2 друг
print("Второй друг", friends[1])
print('Первый друг с конца',friends[-1])

#срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])

print(friends)
#длинна списка
print(len(friends))
#можно добавить в список
friends.append("Ron")
print(friends)
print(len(friends))

#удаляем из списка по умолчанию команда удаляет последнего
print(friends.pop())
print(friends)

# очистить весь список
print(friends.clear())
print(friends)

friends = ["Max","Leo","Kate"]
#можно удалить конкретное значение из списка
friends.remove("Kate")
print(friends)

# удаление с помощью индекса
del friends[0]
print(friends)

#проверяем наличие в строке
hero = 'Superman'
if hero.find('man') != -1:
    print("Есть")
if "man" in hero:
    print('Yes')

goals = ['Статья гуру языка Python',"здоровье","накормить кота"]
if "здоровье" in goals:
    print("YES")

#пишем прогу
print("СОРЕВНОВАНИЯ ПО PYTHON")
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input("Кто занял {} место: ".format(i))
    members.append(name)
    i-=1
#кто участвовал в соревновании по алфавиту
print("В соревновании участвовали: ", sorted(members))

# развернуть список от конца к началу
members.reverse()
#нужно взять первые 3 места
result = members[:3]
result = "Победители {}. Поздравляем!".format(result)
print(result)
