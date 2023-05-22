import random

print('Привет. Загадай число от 1 до 100, а я попробую его угадать')
#print('Но ты должен мне подсказывать символами < > =')
print('Итак, загадайте число, но не говорите его мне')
min = 1
max = 100
number = random.randint(min,max)
result = input(f'Давайте начнем, Вы загадали число {number}? ')

count = 1
while result != "угадал":
    if result == 'больше':
        count += 1
        min = number + 1
        number = random.randint(min,max)
        print(f'Ваше число {number} ?')
        result = input('Я угадал Ваше число ? Введите результат: ')
    elif result == 'меньше':
        count += 1
        max = number - 1
        number = random.randint(min,max)
        print(f'Ваше число {number} ?')
        result = input('Я угадал Ваше число ? Введите результат: ')
    else:
        result = input('Вы можете писать только "больше", "меньше" или "угадал"')
print(f'Отлично ваше число: {number}, а мне потребовалось {count} ходов чтобы его отгадать!')
