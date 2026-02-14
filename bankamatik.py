#Bankamatik Uygulaması

AliHesap = {
    'ad': 'Ali Yılmaz',
    'hesapNo' : '1234568',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

MehmetHesap = {
    'ad': 'Mehmet Öz',
    'hesapNo' : '7896543',
    'bakiye' : 5000,
    'ekHesap' : 4000
}

def paraCek(hesap,miktar):
    print(f"Merhaba, {hesap['ad']}")

    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz")
        bakiyeSorgula(hesap)
    else: 
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if(ekHesapKullanimi == 'e'):
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")

        else:
            print("üzgünüz bakiye yetersiz")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL bulunmaktadır')


paraCek(AliHesap,3000)

print('*'*20)

paraCek(MehmetHesap,1000)
