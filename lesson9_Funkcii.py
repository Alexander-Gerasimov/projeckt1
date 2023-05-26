# модуль числа
print(abs(-7))

# min and max
numbers = [5 , 15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

# round округляет число после запятой указывается число и количество знаков
print(round(10.9872, 2))

# sum просто суммирует все числа из последовательности
print(sum(numbers))

# enumerate переберает элементы
winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)

print('---------------------------------------------------------------------------------------------------')

#пользователь вводит 3 числа.
#найти минимальное из них, максимально, их сумму и вывести результат
numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
