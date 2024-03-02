x=0
while x<10:
    print(x)
    x=x+1

benimListem=[1,2,3,4,5]
while 3 in benimListem:
    print("3 hala listenin icerisinde")
    benimListem.pop()


numara=0
while numara<5:
    if numara==4:
        break
    print(numara)
    numara=numara+1


yeniDegisken=0
while yeniDegisken<15:
    print("yeni degiskenin guncel degeri: " + str(yeniDegisken))
    # ustteki 'yeniDegisken' degiskenine tur donusumu uyguladık. Bir diger yontemde asagida yorum satirinda gosterilmistir.
    # print(f"yeniDegisken'in guncel degeri: {yeniDegisken}")
    yeniDegisken=yeniDegisken+1

    
    