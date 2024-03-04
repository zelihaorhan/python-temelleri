class SuperKahraman():
    def __init__(self,isim,yas,meslek): #init fonksiyonu, siniftan nesne olusturuldugu anda tetiklenir. Icerisindeki self argumanı verilmek zorunda olan bir argumandir. Diger argumanları biz bu ornek icin kendimiz yazdık.
        print("init cagrildi.")
        self.isim=isim  #burda self'in yanındaki degiskenler class'ın kendi argumanlaridir(init fonksiyonu icerisindeki) Esitligin karsi tarafindakiler ise bizim gonderdigimiz degerlerdir.
        self.yas=yas
        self.meslek=meslek
    def ornekMetot(self):
        print(f"Ben super kahramanim ve meslegim: {self.meslek}")
        
class Kopek():
    yilCarpani=7
    def __init__(self,yas=5): # burada yas degiskenine default bir deger atadik, diyelim nesne olusturma surecinde herhangi bir deger girmezsek bu degeri alir, bunun yani sira bir baska deger nesne uretim asamasinda verilebilir.
        self.yas=yas
    def InsanYasiniHesapla(self):
        return self.yas*self.yilCarpani;


superman=SuperKahraman("Superman",30,"Gazeteci");
print(superman.isim)
superman.isim="Clark Kent" #nesne olusturma surecindeki atadığımız degeri bu sekilde degistirebiliriz.
print(superman.isim)
print(superman.ornekMetot())


benimKopek=Kopek(3)
print(benimKopek.yas)
print(benimKopek.InsanYasiniHesapla())










