# try - except - else - finally

# try:
# => Hata olusabilecek kod blogu
#

# except HataTuru1 as hata:
# => HataTuru1 turundeki hatalar icin islemler
# => hata adindaki bir degisken, yakalanan hatanin detaylarini icerir.

# except HataTuru2 as hata:
# => HataTuru2 turundeki hatalar icin islemler

#else:
# => Hata olusmazsa calisacak kod blogu 

#finally:
# => Her durumda calisacak kod blogu



while True:
    try:
        sayi=int(input("Bir sayi girin: "))
        sonuc=10/sayi
        print(f"Sonuc: {sonuc}")
    except ValueError:
        print("Lutfen bir sayi giriniz.")
        continue
    except ZeroDivisionError:
        print("Sifira bolme hatasi.")
    else:
        print("Hata olusmadi")
        break
    finally:
        print("Islem tamamlandi.")