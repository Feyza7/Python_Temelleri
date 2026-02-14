x = 1

while x <= 100:
    if x % 2 == 0:
        print(f"{x} sayısı çifttir")
    else:
        print(f"{x} sayısı tektir")
    x += 1

name = '' #False
while not name.strip():
    name = input("isim: ")
print(f"merhaba, {name}")