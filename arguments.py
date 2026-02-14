def changeName(n):
    n = 'asd'

name = 'feyza'

changeName(name)
print(name)

# orijinal listenin adresi göderilip değiştirilir. 
# kopya liste oluşmaz. liste değişir
def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']

change(sehirler)
print(sehirler)

change(sehirler[:]) #kopyalama ,orijinal liste değişmez
print(sehirler)

#******************************

def add(a, b, c = 0):
    return sum((a,b,c))

print(add(20,50))
print(add(40,60,10))

def topla(*params):
    print(params)
    return sum(params)

print(topla(10,20,30,70))
print(topla(10,80))


def carp(*params):
    carpim = 1
    for n in params:
        carpim *= n
    return carpim

print(carp(1,5,4))
print(carp(2,5,8))


def displayUser(**args): # ** dicitonary olduğunu belirtir
    print('*'*20)
    for key, value in args.items():
        print('{} is {}'.format(key,value))


displayUser(name = 'ali', age =25, city='istanbul')
displayUser(name = 'mehmet', age =35, city='kocaeli',phone='123456')
displayUser(name = 'ayse', age =36, city='izmir',phone='458765', email='ayse@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(20, 40, 50, 70, 80, key1='value1', key2='value2')

