import random

class Boss():
    def __init__(self,nazwa,akt,poziom):
        self.nazwa = nazwa
        self.akt=akt
        self.poziom = poziom

        self.hp = 10*self.poziom*(10**self.akt)
        self.dmg = 10+self.poziom+self.akt*5

    def otrzymywane_obrazenia(self,obrazenia):
        self.aktualne_hp -= obrazenia
    
    def czy_zyje(self):
        return self.aktualne_hp>0
    
    def atak(self,przeciwnik):
        mnoznik_obrazen = round(random.uniform(1.4,1.5),2)
        obrazenia = mnoznik_obrazen*self.dmg
        przeciwnik.otrzymywane_obraznia(obrazenia)

poziomy_trudnosci = {
    "latwy": [Boss("11",1,1),
              Boss("12",1,2),
              Boss("13",1,3),
              Boss("14",1,4),
              Boss("15",1,5)],
    "sredni": [Boss("21",2,1),
              Boss("22",2,2),
              Boss("23",2,3),
              Boss("24",2,4),
              Boss("25",2,5)],
    "trudny": [Boss("31",3,1),
              Boss("32",3,2),
              Boss("33",3,3),
              Boss("34",3,4),
              Boss("35",3,5)],
    "bardzo_trudny": [Boss("51",5,1),
              Boss("52",5,2),
              Boss("53",5,3),
              Boss("54",5,4),
              Boss("55",5,5)]


}