'''
girilen bir sayının asal olup olmadığını bulun
'''

sayi = int(input("bir sayı giriniz: "))

asalMi = True

if(sayi == 1):
    asalMi = False

for i in range(2,sayi):
    if(sayi % i == 0):
        asalMi = False
        break

if asalMi:
    print(f"{sayi} sayısı asal sayıdır.")
else:
    print(f"{sayi} sayısı asal sayı değildir.")