'''
1 ile 100 arasında rastgele üretilecek bir sayıyı 
aşağı yukarı ifadeleri ile buldurmaya çalışın
    "random modülü" için "python random" şeklinde arama yapın
    100 üzerinden puanlama yapın. her soru 20 puan
    hak bilgisini kullanıcıdan alın ve her soru belirtilen 
    can sayısı üzerinden hesaplansın


'''
import random

number = random.randrange(1,100)

hak = int(input("bu sayıyı bulmak için kaç hak istersiniz: "))
i = 1
while(i <= hak):
    tahmin = int(input(f"{i}. tahmin: "))
    if(tahmin == number):
        print(f"tebrikler sayıyı {i}. denemede buldunuz!! Puanınız: {100 - ((100/hak)*(i-1))}")
        break
    elif(tahmin < number):
        print("yukarı")
    elif(tahmin > number):
        print("aşağı")
    i+=1
if(hak < i):
    print(f"üzgünüm hakkınız bitti sayıyı bulamadınız. sayı: {number}")
