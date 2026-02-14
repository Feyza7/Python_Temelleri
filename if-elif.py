x = int(input("bir sayı giriniz: "))
y = int(input("bir sayı giriniz: "))

if x > y:
    print(f"{x} {y}den büyük")
elif x == y:
    print(f"{x} ve {y} eşittir")
else: 
    print(f"{y} {x}den büyük")


a = int(input("bir sayı giriniz: "))
if a > 0:
    print(f"{a} bir pozitif sayıdır")
elif a < 0:
    print(f"{a} bir negatif sayıdır")
else: 
    print(f"{a} sıfırdır")

