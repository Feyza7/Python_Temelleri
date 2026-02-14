#1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluştur
car_list = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(car_list)

#2- liste kaç elemanlıdır
print(len(car_list))

#3- listenin ilk ve son elemanı
print(car_list[0])
print(car_list[len(car_list)-1])

#4- Mazda değerini Toyota ile değiştirin
car_list[-1] = 'Toyota'
print(car_list)

#5- Mercedes listenin bir elemanı mıdır
print('Mercedes' in car_list)

#6- listenin -2 indeksindeki değer 
print(car_list[-2])

#7- listenin ilk 3 elemanınu alın
print(car_list[0:3])

#8- listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
car_list[-2:] = ['Toyota', 'Renault']
print(car_list)

#9- listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
print(car_list + ['Audi', 'Nissan'])

#10- listenin son elemanını silin
del car_list[-1]
print(car_list)

#11- liste elemanlarını tersten yazdırın
print(car_list[::-1])

#12- aşağıdaki verileri bir liste içinde saklayınız

    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet',  'Turan', 1998, [80,70,90]]

#13- liste elemanlarını ekrana yazdırınız
print(studentA[0])
print(studentB[1])
print(studentC[3][1])

print(f"{studentA[0]} {studentA[1]} {2025-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}")
