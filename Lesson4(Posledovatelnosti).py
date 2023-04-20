friend_name = "Max"
friends = ["Max","Leo","Kate"]
Roles = ("admin","quest","user")

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i +=1

# метод FOR самый удобный
for friend in friends:
    print(friend)
print("END 1")

for letter in friend_name:
    print(letter)
print("END 2")

for role in Roles:
    print(role)
print("END 3")
