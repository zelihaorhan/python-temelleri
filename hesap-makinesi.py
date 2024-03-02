def hesapla(a,b,islem):
    if islem not in "+-*/":
        return "Lutfen su islemlerden birini seciniz: +-*/"
    if islem == "+":
        return (str(a) + " "+ " + " + str(b) + " " + " = " + str(a+b))
    if islem == "-":
        return (str(a) + " "+ " - " + str(b) + " " + " = " + str(a-b))
    if islem == "*":
        return (str(a) + " "+ " * " + str(b) + " " + " = " + str(a*b))
    if islem == "/":
        return (str(a) + " "+ " / " + str(b) + " " + " = " + str(a/b))
    
#python'da hata kontrolu try-expect bloklari sayesinde yapilir. try icine hataya sebep olabilecek kodlari, expect icine olasi hatalarda kullaniciya verilecek hata mesaji yazilir.

while True:
    try:
        a=int(input("ilk sayiyi giriniz:"))
        b=int(input("ikinci sayiyi giriniz:"))
        islem=input("Isleminizi seciniz: +-*/")
        print(hesapla(a,b,islem))
    except:
        print("Lütfen sayilari duzgun giriniz...")

    
