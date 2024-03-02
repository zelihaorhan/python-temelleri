#asagidaki ornekte bir stringin tum harflerini ayrı ayrı elde ederek bos bir listeye attık. Boylelikle stringin harflerini iceren bir liste elde etmis olduk.
listeOrnegi=[]
benimString="atıl samancıoğlu"

for harf in benimString:
    listeOrnegi.append(harf)

print(listeOrnegi)

#yukarıda yaptigimiz ornegin bir diger gosterimi asagidaki gibidir.(daha cok yukaridaki yazim tercih edilir.)

yeniString="atıl samancıoğlu"
yeniListeOrnegi=[eleman for eleman in yeniString]
print(yeniListeOrnegi)

