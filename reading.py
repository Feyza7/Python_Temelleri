# "r": (Read) okuma. varsayılan dosya konumunda yoksa hata verir
# try:
#     file = open("newfile3.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()

file = open("newfile.txt","r",encoding = "utf-8")

#okuma yapma işlemleri

#for döngüsü
    
# for i in file:
#     print(i, end= "")

# read() fonksiyonu 

# content = file.read(2)
# content = file.read(5)
# print(content)

# readline() fonksiyonu ile okuma => her defasında tek satır okur

# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

liste = file.readlines()

print(liste)

file.close()