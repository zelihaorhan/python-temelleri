isimStringi="Atıl Samancıoglu"

#index
print(isimStringi[0]) #stringin ilk harfi

#indexleme sirasinda bosluk da bir karakter olarak kabul edilir.

print(isimStringi[-1]) # sondaki ilk harf

print(isimStringi[0]+isimStringi[1]) #iki index toplanabilir. (indexteki karakterler toplanmis olur)


yeniString = "0123456789"
print(yeniString[2:]) # 2.indexten itibaren kalanini yazdirdi. (2.index dahil)
print(yeniString[:3]) # 3.indexe kadar yazdirdi. (3.index dahil degil)

gelenVeri="AhmetinYasi65"
print(gelenVeri[-2:]) # sadece sondaki 65 sayisini ekrana yazdirdi.
print(gelenVeri[2:4]) #2.indexten baslayarak 4.indexe kadar yazdirdi (baslangic indexi dahil, bitis indexi dahil degil)

#step-size
print(gelenVeri[::]) #stringi kendisini oldugu gibi yazdirir
print(gelenVeri[1:10:3]) # 3 er 3 er atlayarak ekrana yazdirir (ilk yazilan => baslangic indexi, ikinci yazılan => bitis indexi, ucuncu yazilan =>atlama indexi)
print(gelenVeri[::-1]) #stringi tersten yazdi
