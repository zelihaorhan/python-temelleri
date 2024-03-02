# range metodu: metodun parantezi icine yazılan sayılar arası bir aralık olusturmaya yarar.

print(list(range(15))) # 0'dan 15'e kadar bir liste olusturdu.

for numara in list(range(15)):
    print(numara*5)

print(list(range(5,22,4))) # 5: baslangic siniri, 22: bitis siniri, 4: atlama degeri


#enumerate metodu: bir iterable nesne(liste,demet,dize vb.) uzerinde dongu yaparken, her bir ogenin dizinini(indeksini) ve degerini eslestiren bir sayici nesnesi uretir. Bu, ozellikle bir dongu icinde hem ogenin degerine hem de indeksine ihtiyac duyuldugu durumlarda kullanislidir.
index = 0
for numara in list(range(5,15)):
    print(f"guncel numara: {numara} guncel index: {index}")
    index=index+1

for eleman in enumerate(list(range(5,15))):
    print(eleman)


#randint metodu: aslında bir metot degil bir kutuphanedir. Rastgele sayi uretmede kullanilir. (bu metodu kullanabilmek icin random kutuphanesi import edilmelidir.)

from random import randint
print(randint(0,100))  # 0 ile 100 arasinda rastgele sayi uretmede kullanilir.

yeniListe=list(range(0,10))
print(yeniListe)
print(yeniListe[randint(0,9)])

#suffle metodu: bir liste veya benzeri bir veri yapisindaki ogeleri rastgele siraya dizer. Ozellikle bir liste icindeki ogelerin siralanmasini rastgele degistirmek istedigimizde kullanilir. (bu metodu kullanabilmek icin random kutuphanesi import edilmelidir.)

from random import shuffle 
print(shuffle(yeniListe))

#zip metodu: bir veya daha fazla iterable nesneyi alir ve bunlari birlestirerek bir tuple dizisi olusturur. Olusturulan her tuple, her bir iterable nesnenin karsilikli ogelerini icerir. Eger verilen iterable nesnelerin uzunlukları farkli ise, 'zip()' fonksiyonu en kisa olan iterable'in uzunlugu kadar eslestirme yapar.

yemekListesi=["muz","ananas","elma"]
kaloriListesi=[100,200,300]
gunListesi=["pazartesi","sali","carsamba"]

ziplenmisListe=list(zip(yemekListesi,kaloriListesi,gunListesi))

print(ziplenmisListe)






