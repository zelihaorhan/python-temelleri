# fonksiyon tanimlamasi 'def' keyword'u ile yapilir. def'in ardindan fonksiyonAdi() yazilir. (eger fonksiyonun parametreleri varsa fonksiyonun parantezleri icine yazilabilir.)

def ilkFonksiyon(): # fonksiyonu tanimladik
    print("İlk fonksiyonum.")

#fonksiyon tanimlandiktan sonra kullanilmak istenildigi yerde cagirilmalidir.

ilkFonksiyon() # fonksiyonu cagirdik


# FONKSIYONLARDA GIRDI & CIKTI

def merhabaDunya(yazdirilacakIsim):
    print("merhaba")
    print(yazdirilacakIsim)
 
merhabaDunya("python")

#geriye deger dondurmeyen bir fonksiyon cagrildigi yerde bir degiskene atansa bile sonradan bu degisken cagrildiginda 'none' doner.
def supertoplama(num1,num2,num3):
    print(num1+num2+num3)
supertoplama(10,20,30)


#geriye deger donduren fonksiyonlar cagrildiklarinda bir degiskene atanmaları gerekir, yoksa fonksiyon calismaz.
def dondurmeliToplama(num1,num2):
    return num1+num2

sonuc=dondurmeliToplama(10,20)
print(sonuc)


def kontrolFonksiyon(s):
    if s=="atıl":
        print("verdiginiz string atıl")
    else:
        print("verdiginiz string baska bir sey")

kontrolFonksiyon("atıl")
kontrolFonksiyon("python")


# args & kwargs

# args: fonksiyonun parametre sayisini developer degil, kullanici belirler.
def yeniToplama(*args):
    return sum(args) 

toplam=yeniToplama(10,20,30,40)
print(toplam)


def benimFonksiyonum(*args):
    print(args)

benimFonksiyonum("zeliha")


# kwargs: fonksiyon parametrelerine anahtar kelime-deger verilecegi zaman kullanilabilir.

def ornekFonksiyon(**kwargs):
    return(kwargs)

cikti=ornekFonksiyon(muz=100,elma=200,ananas=300)
print(cikti)

def keyWordKontrolu(**kwargs):
    if "atıl" in kwargs:
        print("Atıl var")
    else:
        print("Atıl yok")

keyWordKontrolu(ahmet=70,zeynep=20,mehmet=40)