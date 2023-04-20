#friends = ['Max','Leo','Kate']
#print(friends)
#print(type(friends))
#friend = friends[0]
#print(friend)
#print(type(friend))

#как добавить другу возраст ?
friend = {
    'name': 'Max',
    'age': 30
}
print(friend)
print(type(friend))
#получить значение по ключу
print(friend['age'])

#добавляем ключ в уже созданный список
friend['has_car']=True
print(friend)

#можно заменить в словаре если уже есть чтото
friend['has_car']=False
print(friend)

#удаляем ключ из списка
del friend['age']
print(friend)

#  с помощью if можно проверить что есть в ключе и списке
if 'age' in friend:
    print('есть возраст')

if 'has_car' in friend:
    print('есть машина')
print('END -----------------------------------------------------------------------------------')


#перебор словоря с помощью for
friend = {
    'name': 'Max',
    'age': 30,
    'has_car': True
}

#по ключам
for key in friend.keys():
    print(key)
    print(friend[key])
# вариант без точка кейс тоже будет работать
#for key in friend.keys():
   # print(key)
   # print(friend[key])

print("по ключам все---------------------------------------")
# по значения
for val in friend.values():
    print(val)
print('по значениям все -------------------------------------------------')
print('пары ключи значения')
for item in friend.items():
    print(item)

print('искать сразу 2 переменные')
for key,val in friend.items():
    print(key)
    print(val)
