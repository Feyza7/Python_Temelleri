# r+ yerine q kullansaydık dosyanın içindeki her şeyi silip deneme yazardı
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# *********** SAYFA SONUNDA GÜNCELLEME ****************** 

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nMichael Scott")

# ************* SAYFA BAŞINDA GÜNCELLEME ****************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "jim halpert\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

# ************* SAYFA ORTASINDA GÜNCELLEME ****************

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Ahmet Yılar\n")
    file.seek(0)
    # for i in list:
    #     file.write(i) ya da 
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
