# () ile tanimlanir.
# tuple tanimlandiktan sonra elemanlari bir daha degistirilemez.

benimListem={1,2,"a",4.5}
print(benimListem[0])
benimListem[0] = 100 #listelerde eleman degisimi vardi.
print(benimListem)  

benimTuple=(1,2,"a",4.5)
print(benimTuple)
print(benimTuple[0])
print(benimTuple.count("a")) # icine yazilan elemanin kac tane oldugunu bulur.
print(benimTuple.index(4.5)) # icine yazilan elemanin kacinci indexte oldugunu bulur.
benimTuple[2]="b" # hata verir, tuple'daki elemanlar degistirilemez.
print(benimTuple)

