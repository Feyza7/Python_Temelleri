"""
    Daire Alanı   : πr^2
    Daire Çevresi : 2πr

    Yarı çağı girilen bir dairenin alan ve çevresini hesaplayınız. (π = 3.14)

"""
pi = 3.14
r = input("Yarıçap : ")
r = float(r)

daireAlan  = pi *( r ** 2)
daireCevre = (2 * pi * r)

print("Alan    :",daireAlan)
print("Çevre   :",daireCevre)