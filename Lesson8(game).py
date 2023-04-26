# загадать случайное число с помощью встроенной в питон функции рандом
import random

#задаем параметры для рандома от какого до какого искать
number = random.randint(1 , 100)
print(number)


user_number = None
count = 0
levels = {}
max_count = 3
# нужно сделать цикл
while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли.')
        break
    print(f'Попытка  № {count}')
    #далее предлагаем пользователю ввести (загадать) число
    user_number = int(input('Введите число: '))
    #сравнение числе рандома и того что напишет пользователь
    if number < user_number:
        print('Ваше число больше загаданного.')
    elif number > user_number:
        print('Ваше число меньше загаданного.')
else:
    print('Победа')
