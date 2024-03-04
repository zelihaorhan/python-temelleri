#KALITIM

class Hayvan():
    
    def __init__(self):
        print("hayvan sinifi init cagrildi.")
    
    def method1(self):
        print("hayvan sinifi method1 cagrildi.")
    
    def method2(self):
        print("hayvan sinifi method2 cagrildi.")

benimHayvanim=Hayvan() # hayvan sinifindan nesne olusturuldu.
benimHayvanim.method1()
benimHayvanim.method2()

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi sinifi init cagrildi.")
    def miyavla(self):
        print("miyav")
    def method1(self):
        print("kedi sinifindaki method1 cagrildi.")
        
benimKedi=Kedi() # kedi sinifindan nesne olusturuldu.
benimKedi.method1()
benimKedi.miyavla()        

