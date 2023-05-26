def my_f(my_var):
    my_var=999
    print('Внутри функции: ', my_var)

a = 1
my_f(a)
print('После выполнения функции: ', a)

def some_f():
    a=999
    print('Внутри функции: ', a)

a = 1
some_f()
print('После выполнения функции: ', a)

# чтобы обьявить глобальную переменную внутри функции пишем global и задаем ее =

print('-' * 150)
# учимся добавлять функцию в функцию

def some_g():
    return 10

resulr = some_g()
print(resulr)

a= some_g
print(a)
print(type(a))
print(a())
print('-' * 150)

def f():
    print('Hello from other f')

def to(f_param):
    #параметром будет функция
    #поэтому в теле функции to мы ее вызовем
    f_param()
#проверим
to(f)

print('-' * 150)
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(number):
    return number % 2 ==0


print(my_filter(numbers, is_even))

# если нужны нечетные числа
def is_not_even(number):
    return number % 2 != 0


print(my_filter(numbers, is_not_even))
# если нужны числа >4
def big_4(number):
    return number > 4


print(my_filter(numbers, big_4))

print('-' * 150)
#lambda функции
print(my_filter(numbers,lambda number: number % 2 == 0))
print(my_filter(numbers, lambda number: number % 2 != 0))
print(my_filter(numbers, lambda number: number > 4))

print('-' * 150)
# набор числе
numbers2 = [1, 5, 3, 5, 9, 7, 11, 15, 18, 14, 21, 12]
# сортировка по возрастанию
print(sorted(numbers2))
#сортировка по убыванию
print(sorted(numbers2, reverse=True))

# набор строк
names = ['Max','Leo','Kate','Sasha','Angelina']
#сортируем по алфавиту
print(sorted(names))

# города и численность населения
cities = [('Москва', 1000), ('Лас-Вегас', 500),('Антверпен', 2000)]
# данная сортировка отсортирует только по алфавиту
print(sorted(cities))
# как отсортировать по численности населения?
def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))
#либо тоже самое с lambda
print(sorted(cities, key=lambda city: city[1]))

print('-' * 150)
numbers3 = (1, 5, 3, 5, 9, 7, 11, 15, 18, 14, 21, 12)
#получить только четные числа
def is_good(number):
    return number % 2 == 0

result = filter(is_good, numbers3)
print(result)
result= list(result)
print(result)

names2 = ['Max','Leo','Kate','Sasha','Angelina']
print(list(filter(lambda x: len(x)>3, names2)))

print('-' * 150)
# функция map
numbers3 = [1, 5, 3, 5, 9, 7, 11, 15, 18, 14, 21, 12]
# получить список квадратных числе
print(list(map(lambda x: x**2, numbers3)))
#приведем числа к строке
print(list(map(lambda x: str(x), numbers3)))
