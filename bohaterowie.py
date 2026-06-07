import random
class Bohater:
    def __init__(self,inteligencja,sila,zrecznosc,hp):
        self.inteligencja = inteligencja
        self.sila=sila
        self.zrecznosc = zrecznosc

        self.max_hp = hp
        self.aktualne_hp = hp

        self.punkty_umiejetnosci = 0

    def otrzymywane_obrazenia(self,obrazenia):
        self.aktualne_hp = max(0, int(self.aktualne_hp - obrazenia))

    def atakuj(self, przeciwnik):
        obrazenia = self.oblicz_obrazenia()
        przeciwnik.otrzymywane_obrazenia(obrazenia)
    
    def czy_zyje(self):
        return self.aktualne_hp>0
    
class Mag(Bohater):
    def __init__(self,inteligencja, sila, zrecznosc, hp):
        super().__init__(inteligencja, sila, zrecznosc, hp)
        
    def oblicz_obrazenia(self):
        mnoznik_obrazen = random.uniform(1.8,2.2)
        obrazenia = int(mnoznik_obrazen*self.inteligencja)
        return obrazenia

class Wojownik(Bohater):
    def __init__(self, inteligencja, sila, zrecznosc, hp):
        super().__init__(inteligencja, sila, zrecznosc, hp)

    def oblicz_obrazenia(self):
        mnoznik_obrazen = random.uniform(1.2,1.4)
        obrazenia = int(mnoznik_obrazen*self.sila*1.5)
        return obrazenia

class Lucznik(Bohater):
    def __init__(self, inteligencja, sila, zrecznosc, hp):
        super().__init__(inteligencja, sila, zrecznosc, hp)

    def oblicz_obrazenia(self):
        mnoznik_obrazen = random.uniform(1.0,1.😎
        obrazenia = int(mnoznik_obrazen*self.zrecznosc*1.3)
        return obrazenia
