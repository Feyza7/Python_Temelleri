def sayHello(name = 'user'):
    print("hello "+name)

sayHello('Feyza')
sayHello('Etiyen')
sayHello()

#*******************************

def say_hello(name = 'user'):
    return 'Hello dear, '+name

msg = say_hello('prenses sofia')

print(msg)

#*******************************
def topla(a,b):
    return a+b

toplam = topla(5,8)
print(toplam)

#*******************************

import datetime

day = datetime.date.today()

def yasHesapla(dogumYili):
    return  (day.year) - dogumYili

age = yasHesapla(2004)
print(age)

#********************************

def emeklilikHesapla(dogumYili, isim):
    ''' 
    DOCSTRING: doğum yiliniza göre emekliliğinize kaç yıl kaldı
    INPUT: doğum yili, isim
    OUTPUT: hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if(emeklilik > 0):
        print(f"sevgili {isim} emekliliğinize {emeklilik} yıl kaldı")
    else:
        print(f"sevgili {isim} zaten emekli olmuşsunuz.")

emeklilikHesapla(2004,'feyza')

print(help(emeklilikHesapla))
