# загадать случайное число с помощью встроенной в питон функции рандом
import random

#задаем параметры для рандома от какого до какого искать
number = random.randint(1 , 100)
print(number)


user_number = None
count = 0
levels = {1: 10, 2: 3, 3: 3}

level = int(input('Выберете уровень сложности от 1 до 3: '))

# увеличим количество пользователей
user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    i += 1
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)
print('В игре участвуют:',(users))

max_count = levels[level]
# нужно сделать цикл

is_winner = False
winner_name = None


while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли.')
        break
    print(f'Попытка  № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        #далее предлагаем пользователю ввести (загадать) число
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        #сравнение числе рандома и того что напишет пользователь
        elif number < user_number:
            print('Ваше число больше загаданного.')
        else:
            print('Ваше число меньше загаданного.')
else:
    print(f'Победитель: {winner_name}')
