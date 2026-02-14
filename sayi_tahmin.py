import random

sayi = random.randint(1,100)
deneme = 5
while deneme > 0:
    try:
        tahmin = int(input("tahminizi giriniz: "))
    except ValueError:
        print("hatalı tuşlama")
        continue

    if tahmin == sayi:
        print(f"sayıyı bildiniz tebrikler.")
        break
    elif tahmin < sayi:
        print("daha büyük bir sayı giriniz.")
    else:
        print("daha küçük bir sayı giriniz.")

    deneme -= 1
    print(f"Kalan hak: {deneme}")

if deneme == 0:
    print(f"sayı:{sayi}")
