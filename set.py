# {} ile olusturulur.
# set icerisinde tekrar eden elemanlar yoktur

benimListem=[1,2,3,1,2,3]
print(benimListem)

#listeden set olusturma
benimListeSetim=set(benimListem)
print(benimListeSetim) # listeyi sete cevirdik, fakat sette eleman tekrarı yoktur. Bu yüzden setin icerigi : {1,2,3} olur.
print(type(benimListem))
print(type(benimListeSetim))

benimSet={"a","b","c","a"}
print(type(benimSet))
print(benimSet) # ekran ciktisi: {'a','b','c'}

bosListe=[]
print(type(bosListe))
print(bosListe)
bosListe.append(1)
print(bosListe)

bosSet={}
print(type(bosSet)) # tipi sozluk olarak algılayacak.

benimBosSetim=set()
print(type(benimBosSetim)) #tipi set oldu (yukarıdaki sorun ortadan kalktı)
benimBosSetim.add(10)
benimBosSetim.add(10)
benimBosSetim.add(20)
print(benimBosSetim) # ekran ciktisi: {10,20}
