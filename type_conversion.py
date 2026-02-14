x = input('1.sayı: ')
y = input('2.sayı: ')

#input'tan gelen değer string olarak algılanır

toplam = x + y
print(type(x))
print(type(y))
print('Sayıların Toplamı: ', toplam)

toplam = int(x) + int(y)
print('Sayıların Toplamı: ', toplam)
