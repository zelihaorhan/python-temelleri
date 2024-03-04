# polimorfizm : Ayni isimle ancak farkli siniflar tarafindan farkli sekillerde uygulanan metotlari ifade eder. Bu, cesitli nesnelerin ayni arayuzu kullanarak farkli davranislar sergilemesini saglar. 
#polimorfizm, kodun daha esnek ve uyumlu hale getirilmesine yaardimci olurken, daha az tekrarli kod yazilmasina olanak tanir.

class Elma():
    
    def __init__(self,isim):
        self.isim=isim
    
    def bilgiVer(self):
        return self.isim+ " 100 kaloridir."
    
class Muz():
    
    def __init__(self,isim):
        self.isim=isim
    
    def bilgiVer(self):
        return self.isim + " 150 kaloridir."

elma= Elma("elma")
elma.bilgiVer()

muz=Muz("muz")
muz.bilgiVer()

meyveListesi=[elma,muz]

for meyve in meyveListesi:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(muz)
bilgiAl(elma)