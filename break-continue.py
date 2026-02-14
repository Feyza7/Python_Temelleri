name = 'Etienne'

#döngüden çıkış yapar
for letter in name:
    if letter == 'e':
        break
    print(letter)

#pas geçer
for letter in name:
    if letter == 'e':
        continue
    print(letter)

x = 0
while x<5:
    x+=1
    if x==2:
        continue
    print(x)

x = 0
toplam = 0
while x<=100:
    x+=1
    if(x % 2 == 0):
        continue
    toplam+=x
print(toplam)
    