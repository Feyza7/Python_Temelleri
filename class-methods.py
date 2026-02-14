#class
class Person:
    #class attributes
    address = 'no information'
    #constructor(yapıcı method)
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print('init methodu çalıştı')

    #instance methods
    def intro(self):
        print('say hello. I am '+self.name)

    def calculateAge(self):
        return 2025-self.year

#object (instance)
p1 = Person(name = 'ali' , year = 1990)
p2 = Person('ayse',1993)

p1.intro()
p2.intro()

print(f'ad: {p1.name} yaş: {p1.calculateAge()}')
print(f'ad: {p2.name} yaş: {p2.calculateAge()}')

#updating
p1.name ='ahmet'
p1.address = 'kocaeli'

#accessing object attributes
print(f'name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    #Methods

    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1 = Circle()
c2 = Circle(5)

print(f'c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c1: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')

