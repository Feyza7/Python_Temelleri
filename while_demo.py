# sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın
# n = 0
# while n < len(sayilar):
#     print(sayilar[n])
#     n += 1

# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
# a = int(input("başlangıç değerini giriniz: "))
# b = int(input("bitiş değerini giriniz: "))
# x = a
# while x < b:
#     if x % 2 != 0:
#         print(x)
#     x += 1  

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın
# x = 100
# while x >= 1:
#     print(x)
#     x -=1

# 4- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
# liste = []
# i = 0

# while i<5:
#     sayi = int(input("sayı:"))
#     liste.append(sayi)
#     i+=1
# liste.sort()
# print(liste)

# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın
#     ürün sayısını kullanıcıya sorun
#     dictionary listesi yapısı (name,price) şeklinde olsun
#     ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []
adet = int(input("ürün sayısı: "))
i = 0
while i < adet:
    name = input("ürün ismi: ")
    price = int(input("ürün fiyatı: "))
    urunler.append({
        'name' : name,
        'price': price
    })
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")