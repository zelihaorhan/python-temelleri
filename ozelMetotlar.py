class Meyve():
    
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori
        
    def __str__(self):
        return f"{self.isim} su kadar kaloriye sahiptir: {self.kalori}"
         
    def __len__(self):
        return self.kalori
    
    
muz=Meyve("Muz",150)
print(muz)

print(len(muz))