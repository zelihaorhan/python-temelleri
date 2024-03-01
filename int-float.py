benimDegiskenim=10
benimDigerDegiskenim=20

print(type(benimDegiskenim)) #bir degiskenin hangi turde oldugunu bulmak icin 'type' fonksiyonu kullanilir.

#bir islemin sonucunu bir degiskene atayabiliriz.
sonuc=benimDigerDegiskenim/benimDegiskenim
print(type(sonuc))

a=3
b=2
print(a/b) #sonuc 1.5 olacak yani floattir.

pi=3.14 #python'da float degerler nokta ile yazilir.

#int ve float turdeki degiskenler kendi aralarında matematiksel islemlere tabi tutulabilir
print(a+pi)
print(a*pi)

#MATEMATIKSEL ISLEMLER

x=5
y=10
print(x*y*10) #degiskenler bir sabit sayiyla isleme tabi tutulabilir
print(x*x*x*x) 
print(x**4) # '**' operatoru : uzeri demek demek (x*x*x*x)
print(10%2) # % operatoru: mod alma operatorudur (kalan bulma)


#KULLANICIDAN INPUT ALMAK

input("Yasinizi giriniz:") # bu sekilde direkt kullanicidan bir deger alabiliyoruz.
#kullanicidan aldigimiz degeri bir degisken icinde de tutabiliriz
kullanicininYasi=input("Yasinizi giriniz:")
print(kullanicininYasi)
print(type(kullanicininYasi)) #kullanicidan alinan degerin degisken turu 'string' tir





