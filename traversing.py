# dosya kapatma yöntemi
# file.close() ile aynı
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0) #imleci götürmek istediğimiz konumu verir
    print(file.tell()) #imlecin konumunu verir
    content2 = file.read(10)
    print(content2)

