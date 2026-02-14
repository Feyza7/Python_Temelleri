# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
#        Dosyayı konumda oluşturur.
#        Dosya içeriğini siler ve yeniden ekleme yapar


# file= open("newfile.txt","w")
# file.close()

# dosya oluşturma
# file = open("C:/Users/hp/desktop/newfile.txt","w")

# file = open("newfile.txt","w",encoding = 'utf-8')
# file.write("asd")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding = 'utf-8')
# file.write("asd")
# file.close()
#çalıştırıldığı kadar içerik eklenir

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
file = open("newfile2.txt","x",encoding = 'utf-8')

