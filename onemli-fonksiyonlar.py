def bolmeIslemi(numara):
    return numara/2

print(bolmeIslemi(20))


benimListem=[1,2,3,4,5,6,7,8,9,10]

yeniListe=[]
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
print(yeniListe)


# map: bir listeyle bir fonksiyonu isleme tabi tutup sonucu yine bir listede tutmak istedigimizde kullanabiliriz.

map(bolmeIslemi,benimListem) #ilk parametre olusturdugumuz fonksiyon, ikinci parametre sonucları tutacagimiz liste

def kontrolFonksiyonu(string):
    return "a" in string
print(kontrolFonksiyonu("atıl")) # ekran ciktisi: True
print(kontrolFonksiyonu("zeynep")) # ekran ciktisi: False

stringListesi=["atıl","samancıoglu","atlas","zeynep","mehmet","ahmet","levent"]
sonucListesi=list(map(kontrolFonksiyonu,stringListesi))
print(sonucListesi) 

#filter: parametre olarak  fonksiyon ve bir liste verilir. Liste içinde fonksiyondaki şartı sağlayan degerler yine bir liste olarak dondurulur.

print(list(filter(kontrolFonksiyonu,stringListesi)))


#lambda: fonksiyonları tek satırda yazmaya yarar.
carpma = lambda numara:numara*3
carpma(10)
ornekListesi=[10,20,30]
print(list(map(lambda numara:numara*4,ornekListesi)))





