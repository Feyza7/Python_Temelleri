x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı
sayiA = input("bir sayı giriniz: ")
sayiB = input("bir sayı giriniz: ")

carpim = int(sayiA) * int(sayiB)
toplam = x + y + z
print(carpim - toplam)

# 2- y'nin x'e kalansız bölümünü hesaplama
bolum = y // x
print(bolum)

# 3- (x,y,z) toplamının mod 3'ü nedir
print(toplam % 3)

# 4- y'nin x. kuvvetini hesapla
print(y ** x)

# 5- x, *y, z = numbers işlemine göre z'nin küpü
x, *y, z = numbers
print(z**3)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı
print(y[0]+y[1]+y[2])