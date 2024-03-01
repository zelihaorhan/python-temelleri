# string degiskenler cift tirnak veya tek tirnak arasinda tanimlanirlar.

x="merhaba dunya"
print(x)
print(type(x))

y='yeni string'
print(y)

print(y.capitalize()) #capitalize string'lere ozel bir fonksiyondur, stringin buyuk harfle baslamasini saglar
print(y.split()) #split string'lere ozel bir fonksiyondur, stringi tek tırnakla ayırır (kac kelime varsa hepsini ayırır ve bir liste halinde gosterir)

benimString = "Atıl Samancıoğlu"
print(benimString+y) # + operatoru ile iki stringi toplayabiliriz. (arada bosluk yok)
print(benimString*4) # bir stringi bir sayi ile carpabiliriz (carptigimiz sayi kadar yan yana yazdirir)

#kullanicidan alinan input'un türü default olarak string oldugu icin; kullanicidan sayisal bir deger alindiginda ve bu deger uzerinde matematiksel islemler yapılmak istendiginde bir tur donusumu yapılmalidir. (string=>int)
benimInput=input("Yasinizi giriniz: ") #kullanicidan input alindi.
benimInput=int(benimInput) # alianan input'a tur donusumu yapıldı.
print(benimInput/3*5) # input üzerinde matematiksel islemler yapildi.

k="samancioglu"
print(len(k)) #len fonksiyonu: içine yazılan stringin kac karakterden olustugunu ekrana bastirir.

print("merhaba \npython") #\n: 'new line' demektir, kendinden sonra yazilan ifadeyi bir alt satira alir.







