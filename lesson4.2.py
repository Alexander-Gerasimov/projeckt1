friends_name = "Max"
friends = ["Max","Leo","Kate"]
roles = ("admin","quest","user")

# For
# while

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i +=1

for friend in friends:
    print(friend)
print("END friends")

# вывод символов из строки
for letter in friends_name:
    print(letter)
print("END letter")
