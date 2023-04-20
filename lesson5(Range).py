# в списке рендж 10 чисел
numbers = range(10)
print(numbers)
print(type(numbers))

# отобразим все числа из списка и приведем его к типу лист
print(list(numbers))

#пример функции рендж
winners = ["Max","Leo","Kate"]
#перебор с функцией FOR
for winer in winners:
    print(winer)

# используем range
for i in range(len(winners)):
    #print(i)
    #print(winners[i])
    print(i+1, ")", winners[i])

