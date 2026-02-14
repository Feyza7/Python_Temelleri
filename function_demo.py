# 1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın

# def func(text,number):
#     i = 1
#     while i <= index:
#         print(word)
#         i+=1


# word = input("kelime giriniz: ")
# index = int(input("kaç kere yazdırılsın: "))
# func(word,index)


# 2- kendine gönderilen sanırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın


# def func1(*params):
#     liste = []

#     for param in params:
#         liste.append(param)
#     return liste

# result = func1(20,40,80,10,100,'hello')
# print(result)


# 3- gönderilen 2 sayı arasındaki tüm asal sayıları bulun


# def asalBul(sayi1,sayi2):
    
#     for sayi in range(sayi1,sayi2+1):
#         if(sayi > 1):
#             for i in range(2,sayi):
#                 if(sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input("1.sayıyı giriniz: "))
# sayi2 = int(input("2.sayıyı giriniz: "))
# asalBul(sayi1,sayi2)


# 4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün

def tamBolen(sayi):
    tamBolenler = []
    for i in range(1,sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)
    print(tamBolenler)

    
tamBolen(20)
