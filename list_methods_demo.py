names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1- Cenk ismini listenin sonuna ekle
names.append("Cenk")

#2- Sena değerini listenin başına ekle
names.insert(0,"Sena")

#3- Deniz isminin indeksi nedir
index = names.index("Deniz")
print(index)

#4- Deniz ismini listeden sil
names.remove('Deniz')
print(names)

#5- Ali listenin bir elemanı mıdır
result = "Ali" in names
print(result)

#6- Liste elemanlarını ters çevir
names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sırala
names.sort()
print(names)

#8- year listesini rakamsal büyüklüğe göre sırala
years.sort()
print(years)

#9- str = "Chevrolet, Dacia" karakter dizisini listeye çevir
str = "Chevrolet, Dacia"
result = str.split(',')
print(result)

#10- years dizisinin en büyük ve en küçük elemanı nedir
print(min(years))
print(max(years))

#11- years dizisinde kaç tane 1998 değeri vardır
print(years.count(1998))

#12- year dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
#13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)