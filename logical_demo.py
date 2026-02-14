# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
# a = int(input("bir sayı giriniz:"))
# result = (0 < a) and (a <= 100)
# print(f"{a} sayısı 0 ile 100 arasındadır : {result}")

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
# a = int(input("bir sayı giriniz:"))
# result = (a > 0) and (a % 2 == 0)
# print(f"{a} sayısı pozitif çift sayıdır : {result}")

# 3- email ve parola bilgileri ile giriş kontrolü yapınız
# email = 'asd@gmail.com'
# password = '1234'

# mail = input("mail adresini giriniz: ")
# parola = input("parolayı giriniz: ")

# result = (mail == email) and (parola == password)
# print(f"parola ve email uyuşuyor : {result}")

# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız
# a = int(input("sayi giriniz: "))
# b = int(input("sayi giriniz: "))
# c = int(input("sayi giriniz: "))

# result = (a>b) and (a>c)
# print(f"{a} en buyuk sayıdır : {result}")

# result = (b>a) and (b>c)
# print(f"{b} en buyuk sayıdır : {result}")

# result = (c>a) and (c>b)
# print(f"{c} en buyuk sayıdır : {result}")

# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#     eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#     a-)ortalama 50 olsa bile final notu en az 50 olmalıdır
#     b-) finalden 70 alındığında ortalamanın önemi olmasın

# vize1 = int(input("1.vize notu: "))
# vize2 = int(input("2.vize notu: "))
# final = int(input("final notu: "))

# ort = (((vize1+vize2)/2)*0.6) + (final*0.4)

# result = (ort >= 50) and (final>=50)
# result = (ort >= 50) or (final>=70)

# print(f"ortalama: {ort} geçti mi: {result}")

# 6- kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#     formül: (kilo/boy uzunluğunun karesi)
#     aşağıdaki tabloya göre kişi hangi gruba girmektedir
#     0-18.4 => zayıf
#     18.5-24.9 => normal
#     25.0-29.9 => fazla kilolu
#     30.0-34.9 => şişman

name = input("adınız: ")
kilo = float(input("kilonuz: "))
boy = float(input("boyunuz: "))

index = (kilo) / (boy**2)

zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
fazla_kilolu = (index >= 25.0) and (index <= 29.9)
sisman = (index >= 30.0) and (index <= 34.9)

print(f"{name} kişisinin kilo indeksi: {index} ve kilo değerlendirmesi zayıf: {zayif}")
print(f"{name} kişisinin kilo indeksi: {index} ve kilo değerlendirmesi normal: {normal}")
print(f"{name} kişisinin kilo indeksi: {index} ve kilo değerlendirmesi kilolu: {fazla_kilolu}")
print(f"{name} kişisinin kilo indeksi: {index} ve kilo değerlendirmesi obez: {sisman}")