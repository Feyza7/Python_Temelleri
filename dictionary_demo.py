'''
ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yılmaz',
        'telefon' : '532 000 00 14'
    },
    '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 15'
    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 16'
    }
}

1- bilgileri verilen öğrecileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
2- öğrenci numarasını kullanıcıdan laıp ilgili öğrenci bilgisini gösterin

'''

student = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# student[number] = {
#     'ad' : name,
#     'soyad' : surname,
#     'telefon': phone
# }

student.update({
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon': phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

student.update({
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon': phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

student.update({
    number: {
        'ad' : name,
        'soyad' : surname,
        'telefon': phone
    }
})

print('*'*50)

ogrNo = input("öğrenci no: ")
ogrenci = student[ogrNo]

print(f'Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} telefon numarası: {ogrenci['telefon']}')
