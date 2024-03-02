#break: donguyu kullanıldıgı yerde (varsa sarti sagladigi yerde) sonlandirir.

benimListem=[5,10,15,20,25,30]
for numara in benimListem:
    if numara==15:
        break #dongu 15'e geldiginde sonlandirilir.
    print(numara)
    

#continue: donguyu kullanıldığı yerde (varsa sarti sagladigi yerde) o elemanı atlar ve dongu islemi devam eder.

for numara in benimListem:
    if numara==15:
        continue #dongu 15'e geldiginde 15 atlanir ve dongu devam eder.
    print(numara)


#pass: ya bir islem yapılmaycaksa ya da sonradan tamamlanacak bir yer varsa kullanılır.

for numara in benimListem:
    pass