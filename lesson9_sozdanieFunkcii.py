# обьявим свою функцию
def get_sep(sep, sep_len):
    return sep * sep_len


# меняем знак разделителя
print (get_sep ('-', 100))
print (get_sep ('*', 100))
#меняем знак и длинну
print (get_sep ('/', 50))

# используем разделитель в тексте
sep = get_sep ('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)

def hello_Max():
    print('Hello', 'Max')

hello_Max()

def hello(who):
    print('Hello', who)

hello('sasha')

def greating(who, say):
    print(say, who)
greating('Sasha', 'hellllloooo')

# не верно если поменять местами
greating(' Hello', 'Leo')
greating(say='hi',who='Leo')

def greating2(who, say='Hello'):
    print(say, who)
greating2('Max')
greating2("max", "Privet")

print (get_sep('-', 200))
def greating3(say, *args):
    print(say,args)
greating3('Hello', 'Kate', 'Max', 'Kate','Sasha')
# в первом случае приходит картеж, а во втором словарь

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
get_person(name='Leo', age=20, has_car=True, age_cat=4)