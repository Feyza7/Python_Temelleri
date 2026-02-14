# 1- girilen 2 sayıdan hangisi büyüktür
sayi1 = int(input("sayi giriniz: "))
sayi2 = int(input("sayi giriniz: "))
result = (sayi1 > sayi2)
print(f'sayi1: {sayi1} sayi2: {sayi2} den büyüktür: {result}')

# 2- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesapla eğer ort 50 ve üzeriyse geçti yazsın
vize = int(input("vize notu giriniz: "))
final = int(input("final notunu giriniz: "))

ort = (vize*0.6) + (final*0.4)
result = ort >= 50
print(f"ortalama {ort} ile öğrenci geçmiştir : {result}")

# 3- girilen bir sayının tek mi çift mi olduğunu yazdır
a = int(input("sayi giriniz: "))
b = int(input("sayi giriniz: "))

result = a % 2 == 0
print(f"{a} bir çift sayıdır : {result}")

result = b % 2 == 0
print(f"{b} bir çift sayıdır: {result}")

# 4- girilen bir sayının negatif mi pozitif mi olduğunu yazdır
x = int(input("sayi giriniz: "))
y = int(input("sayi giriniz: "))

result = x > 0
print(f"{x} bir pozitif sayıdır : {result}")

result = y > 0
print(f"{y} bir pozitif sayıdır: {result}")

# 5- parola ve email bilgisini isteyip doğruluğunu kontrol et
e_mail = 'email@asd.com'
password = 1234

email = input("email adresini giriniz: ")
parola = int(input('parolayı giriniz'))

isemail = (email == e_mail.lover().strip())
ispassword = (parola == password)

print(f"mail bilgisi: {isemail}")
print(f"parola bilgisi: {ispassword}")
