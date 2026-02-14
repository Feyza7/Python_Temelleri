website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])

#3- 'website' içinden com karakterlerini alın.
lenght= len(website)
print(website[22:25])
print(website[lenght-3:lenght])

#4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[0:15])
print(course[-15:])

#5- 'course' ifadesindeki karakterleri tersten yazdırın
print(course[::-1])

"""
s = '12345' *5
print(s[::5])

"""

name, surname, age, job = 'Bora' , 'Yılmaz' , 32, 'mühendis'

#6- Yukarıda verilen değişkenler ile ekrana "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")

#7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin
s= "Hello world"
print(s[0:6] + 'W' + s[-4:])
print(s.replace('w' , 'W'))

#8- 'abc' ifadesini yanyana 3 defa yazdırın
s = "abc "
print(s * 3)