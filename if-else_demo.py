# 1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
# name = input("adınız: ")
# age = int(input("yaşınız: "))
# edu = input("eğitim durumunuz: ")

# if (age >= 18):
#     if(edu == 'lise') or (edu == 'üniversite'):
#         print(f"{name} kişisi ehliyet alabilir")
#     else:
#         print(f"{name} kişisi eğitim durumu tutmadığından ehliyet alamaz")
# else:
#     print(f"{name} kişisi yaşı tutmadığından ehliyet alamaz")


# 2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#     0-24 => 0
#     25-44 => 1
#     45-54 => 2
#     55-69 => 3
#     70-84 => 4
#     85-100 => 5

# exam1 = float(input("1.yazılı notu: "))
# exam2 = float(input("2.yazılı notu: "))
# sozlu = float(input("sözlü notu notu: "))

# ort = (exam1 + exam2 +sozlu) /3 

# if (ort >= 0) and (ort <= 24):
#     print(f"ortalama: {ort} not: 0")
# elif (ort >= 25) and (ort <= 44):
#     print(f"ortalama: {ort} not: 1")
# elif (ort >= 45) and (ort <= 54):
#     print(f"ortalama: {ort} not: 2")
# elif (ort >= 55) and (ort <= 69):
#     print(f"ortalama: {ort} not: 3")
# elif (ort >= 70) and (ort <= 84):
#     print(f"ortalama: {ort} not: 4")
# elif (ort >= 85) and (ort <= 100):
#     print(f"ortalama: {ort} not: 5")
# else:
#     print("yanlış tuşlama")


# 3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hsaplayınız
#     1.bakım => 1.yıl
#     2.bakım => 2.yıl
#     3.bakım => 3.yıl
#    süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#    datetime modülünü kullanmanız gerekiyor

import datetime

tarih = input("aracınız  hangi tarihte trafiğe çıktı (2025/01/01): ")
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1.servis")
elif (days > 365) and (days <= 365*2):
    print("2.servis")
elif (days > 365*2) and (days <= 365*3):
    print("3.servis")
else:
    print("hatalı tuşlama")