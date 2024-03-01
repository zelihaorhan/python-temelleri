#sozluklerde, anahtar kelime-deger eslesmesi (key-value pairing) vardir. 
# {} ile olusturulur.

benimSozluk={"anahtarKelime":"deger"}
print(benimSozluk)
print(type(benimSozluk))

benimYemekKaloriSozlugum={"elma":100,"karpuz":200,"muz":300}
print(benimYemekKaloriSozlugum("muz")) # 'muz' key'inin value'si ekrana yazdirilir.

#sozlugun value'ları degistirilebilir
benimYemekKaloriSozlugum["elma"]=500
print(benimYemekKaloriSozlugum)

#key ve value'ların türleri herhangi bir turde olabilir, hangi turde oldugu onemli degildir. (her key veya her value'nun turu birbirinden farklı olabilir)
benimDegisikSOzlugum={150:"atıl", 200:"atlas"}
print(benimDegisikSOzlugum[150])

yeniDictionary={"anahtar1":100,"anahtar2":[10,20,30,40,4.5,"atıl"], "anahtar3":{"anahtar9":4}}
yeniDictionary.keys() #sadece anahtar kelimeleri bir liste icinde gosterir.
yeniDictionary.values() #sadece degerleri bir liste icinde gosterir.
yeniDictionary["anahtar1"][-1] # 'atıl' a ulastik.
yeniDictionary["anahtar3"]["anahtar9"] # 4'e ulastik.

