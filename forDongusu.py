benimListem=[10,20,30,40,50]
print("dongu basladi")
for numara in benimListem:
    print(numara*5/3)
print("dongu bitti.")


yeniListe=[1,2,3,4,5,6]
for rakam in yeniListe:
    if rakam%2==0:
        print(rakam)
    

yeniString="Atıl Samancıoğlu"
for harf in yeniString:
    print(harf)


benimTuple=(1,2,3,4,5)
for eleman in benimTuple:
    print(eleman-10)


koordinatListesi=[(10.2,15.2),(32.4,16,2),(40.2,20.2)]
for eleman in koordinatListesi:
    print(eleman)


benimGaripListem=[(1,2,3),(4,5,6),(7,8,9)]
for (x,y,z) in benimGaripListem:
    print(z)

benimSozluk={"muz":150,"portakal":250,"elma":400}
for(anahtar,deger) in benimSozluk.items():
    print(deger)