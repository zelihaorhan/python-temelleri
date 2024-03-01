# bir veri tipidir.
# sadece 'true' veya 'false' degerini alir..

benimBoolean=True
print(type(benimBoolean))
print(benimBoolean)

# genellikle kıyaslama yaparken kullanilan bir veri tipidir.

listem = [5000,10000,3000,1000,2000,4000]

print(len(listem)) # len fonksiyonu: listenin eleman sayisini dondurur.
print(sum(listem)) # sum fonksiyonu: listedeki elemanlarin toplamini bulur.
ortalama=sum(listem)/len(listem)
print(ortalama)
print(listem[3]>ortalama) # ekran ciktisi: False


maasBilgisi=int(input("Maas bilgisini giriniz:"))
print(maasBilgisi>6000) # ekran ciktisi: True


#KIYASLAMALAR

x=10
y=8
print(x>y) # ekran ciktisi: true
print(x<y) # ekran ciktisi: false
print(x>=y) # ekran ciktisi: true
print(x<=y) # ekran ciktisi: false
print(x==y) # '==' operatoru: 'esit mi' demektir
print(x!=y) # '!=' operatoru: 'esit degil midir' demektir.
print(3>1 and 3>2) # and operatoru için, iki tarafın her ikisinin dogru olması durumunda True, diger tum durumlarda False doner.
print(3>1 or 5<6) # or operatoru için, iki taraftan en az biri dogru oldugunda True, her ikisi yanlıs oldugunda False doner.
print(not 5==4) # ekran ciktisi: True
