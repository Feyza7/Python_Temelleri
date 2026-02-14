website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterleri silin

s = ' Hello World '
s = s.strip()
print(s)

#2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin
result = 'www.sadikturan.com'
result = result.lstrip('www.')
result = result.rstrip('.com')


#3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın

result = course.lower()

#4- 'website' içinde kaç tane a karakteri vardır (count('a))

result = website.count('a')

#5- 'website' www" ile başlayıp com ile bitiyor mu

result = website.startswith('www')
result = website.endswith('com')

#6- 'website' içinde '.com' ifadesi var mı

result = website.find('.com')
result = course.rfind('Python')
result = website.index('com')

#7- 'course' içindeki karakterlerin hepsi alfabetik mi (isalpha, isdigit)

result = course.isalpha()
result = course.isdigit()

#8- 'Contents'ifadesini satırda 50 karakter içinde yerleştirip sağına ve soluna * ekle

result = 'Contents'.center(50,'*')
result = 'Contents'.ljust(50,'*')
result = 'Contents'.rjust(50,'*')

#9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştir

result = course.replace(' ','-')
result = course.replace(' ','-',5)
result = course.replace(' ','')

#10- 'Hello World karakter dizisinin 'World' ifadesini 'There' olarak değiştir

result = 'Hello World'.replace('World', 'There')

#11- 'course' karakter dizisinin boşluk karakterlerinden ayırın

result = course.split(' ')

print(result)