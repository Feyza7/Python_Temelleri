""" 
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgileri
    Müşteri yaşı
"""

musteriAdi = 'Ali'
musteriSoyadi = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyadi
musteriCinsiyet = True #Kadın
musteriTc = '14725836910'
musteriDogumYili = 1985
musteriAdres = 'İstanbul Kadıköy'
musteriyasi = 2025 - musteriDogumYili

print(musteriAdi)
print(musteriSoyadi)
print(musteriAdSoyad)
print(musteriCinsiyet)
print(musteriTc)
print(musteriDogumYili)
print(musteriyasi)
"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3
print("Total: ",total)
