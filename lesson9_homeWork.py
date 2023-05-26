import random
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
def person(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'
print(person('Макс', 21, 'Бостон'))

#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def big(num1, num2, num3):
    return max(num1, num2, num3, key=int)
print(big(1, 2, 8))

#3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#name - строка полученная от пользователя,
#health = 100,
#damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать
# функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. ### Функция в качестве
# аргумента будет принимать атакующего и атакуемого. ### В теле функция должна получить параметр damage атакующего
# и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.


first_player = {
    'first_name' : input("Введите имя первого игрока: "),
    'health': 100,
    'damage': random.randint(0, 100),
     'armor' : 1.2
}

two_player = {
    'two_name' : input("Введите имя второго игрока: "),
    'health': 100,
    'damage': random.randint(0, 100),
    'armor' : 1.2
}
def attack(attack, defence):
    return f"{attack['first_name']} наносит: {attack['damage']} урона " \
           f"и оставляет {defence['two_name']}: {defence['health'] - attack['damage']} хп." \
           f" {defence['two_name']} наносит: {defence['damage']} урона " \
           f"и оставляет {attack['first_name']}: {attack['health'] - defence['damage']} хп."


print(attack(first_player, two_player))

#4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#Наносит урон. Это улучшенная версия функции из задачи 3.
#Вычисляет урон по отношению к броне.

def attack(attack,defence):
    def armor_def():
        damage = attack['damage'] / defence['armor']
        return round(damage, 2)
    def armor_def2():
        damage2 = defence['damage'] / attack['armor']
        return round(damage2, 2)
    return f"{attack['first_name']} наносит: {armor_def()} урона "\
           f"и оставляет {defence['two_name']}: {defence['health'] - attack['damage']} хп. " \
           f"{defence['two_name']} наносит: {armor_def2()} урона" \
           f" и оставляет {attack['first_name']}: {attack['health'] - defence['damage']} хп."\



print(attack(first_player, two_player))


