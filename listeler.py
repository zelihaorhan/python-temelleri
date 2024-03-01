#liste: birden fazla veriyi tutmamizi saglayan veri yapisidir. (tutulan verilerin turleri farkli olabilir)
# [] ile olusturulur.
#listeler mutable(degistirilebilir)'dir. Yani elemanları bir baska elemanla degistirilebilir.
# listede bir eleman birden fazla sayida barindirabilir.

benimListem=[10,20,30,40]
print(type(benimListem))
benimListem[0]=100 # listenin ilk elemanini kalıcı olarak degistirdik.
print(benimListem) 
benimListem.append(50) #sona eleman eklerken 'append' metodu kullanilir.
print(benimListem)

benimNumaram=10
benimDigerNummaram=20
benimNumaraListem=[benimNumaram,benimDigerNummaram]
print(benimNumaraListem[0])


#LISTE METOTLARI

benimListem.pop() # sondaki elemani siler.
benimListem.reverse() # listeyi tersine cevirir.
benimListem.remove(40) # icine yazilan elemani siler. (eger icine yazilan eleman zaten listede yoksa hata verir)
benimListem.count(10) # içine yazilan elemanin listede kac tane oldugunu bulur.


benimStringListem=["Ahmet","Zeynep","Atıl"]
benimDigerListem=["Mehmet", "Mahmut", "Atlas"]
benimToplamaListem=benimStringListem+benimDigerListem #iki liste toplanabilir.
print(benimToplamaListem) 
print(benimStringListem*5) #bir liste bir sayiyla carpilabilir. (kac ile carpiyorsak listeyi o kadar yazdirir)


karisikListe=[1,2,3.5,"atil",9]
print(type(karisikListe))
sonucum = karisikListe[3]
print(sonucum)
print(type(sonucum))


#nested-list: iç içe tanimlanmis liste (liste içinde liste veya listeler tanimlanabilir)
nestedList=[1,5,"atil",4,[6,"z"]]
print(type(nestedList))
zDegiskenimiz=nestedList[4][1] # 'nestedList'in 4.indexine git, 4.indexteki listenin 1.indexini al' demek.
print(zDegiskenimiz)
print(nestedList[:2]) #listenin basindan 2.indexine kadar yazdirir.

karmasikListe=[[1,2,3,["a","b"],50],40,20,["z",5.5],[3,["a"]]]
bDegiskenimiz=karmasikListe[0][3][1]
print(bDegiskenimiz)
