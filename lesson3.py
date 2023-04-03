friend = "Maksim Leonid"
# вывести первую или конечные буквы
first_letter = friend[1]
print("1 bykva",first_letter)
print(friend[-2])

#вывести срез из текста либо до символа, либо кусок, либо от символа до конца
print(friend[1:4])
print(friend[1:])
print(friend[:5])

# определить длину строки
print(len(friend))

#найти символ в строке
print(friend.find("Leo"))

#разбить строку с помощью разделителя
print(friend.split())

#проверить есть ли в строке числа или нет или является ли строка числом
print(friend.isdigit())

#делает все буквы в строке большими
print(friend.upper())

#делает все буквы в строке маленькими
print(friend.lower())

# 3 варианта как слепить текст
# 1 вариант
name = "Alexander"
age = 29
# metod 1 konkatenacia
hello = "Privet, " + name + " tebe " + str(age) + " let "
print(hello)

#metod 2 %
hello = "Privet %s tebe %d let"%(name,age)
print(hello)

# metod 3 .format
hello = "Privet {} tebe {} let".format(name,age)
print(hello)

top5 = "Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов"
#Поздравляем 1. иванов 2. петров 3. сидоров с успехом!
start = top5.find("1")
end = top5.find("4")

top3 = top5[start:end]
result = "Поздравляем {} с успехом!".format(top3.upper())
print(result)

