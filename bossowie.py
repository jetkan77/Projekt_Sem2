import random
import pygame
class Boss():
    def __init__(self,nazwa,akt,poziom,nazwa_pliku_grafiki):
        self.nazwa = nazwa
        self.akt=akt
        self.poziom = poziom

        self.max_hp = int(50+(self.akt-1)*150+self.poziom*30*self.akt)
        self.aktualne_hp = self.max_hp
        self.dmg = 10+self.poziom+self.akt*5

        self.plik_grafiki = nazwa_pliku_grafiki
        self.grafika = None

    def otrzymywane_obrazenia(self,obrazenia):
        self.aktualne_hp = max(0, int(self.aktualne_hp-obrazenia))
    
    def czy_zyje(self):
        return self.aktualne_hp>0
    
    def atak(self,przeciwnik):
        mnoznik_obrazen = round(random.uniform(1.4,1.5),2)
        obrazenia = mnoznik_obrazen*self.dmg
        przeciwnik.otrzymywane_obrazenia(obrazenia)
    
    def rysuj(self, screen, x, y):
        if self.grafika is None:
            self.grafika = pygame.image.load(f"grafiki/{self.plik_grafiki}").convert_alpha()
            docelowy_rozmiar = (200, 200)
            self.grafika = pygame.transform.scale(self.grafika, docelowy_rozmiar)
            self.grafika.set_colorkey((255, 255, 255))
        screen.blit(self.grafika, (x, y))
poziomy_trudnosci = {
    "Latwy": [Boss("Goblin",1,1,"Goblin.png"),
              Boss("12",1,2,"Goblin.png"),
              Boss("13",1,3,"Goblin.png"),
              Boss("14",1,4,"Goblin.png"),
              Boss("15",1,5,"Goblin.png")],
    "Sredni": [Boss("21",2,1,"Goblin.png"),
              Boss("22",2,2,"Goblin.png"),
              Boss("23",2,3,"Goblin.png"),
              Boss("24",2,4,"Goblin.png"),
              Boss("25",2,5,"Goblin.png")],
    "Trudny": [Boss("31",3,1,"Goblin.png"),
              Boss("32",3,2,"Goblin.png"),
              Boss("33",3,3,"Goblin.png"),
              Boss("34",3,4,"Goblin.png"),
              Boss("35",3,5,"Goblin.png")],
    "Epicki": [Boss("51",4,1,"Goblin.png"),
              Boss("52",4,2,"Goblin.png"),
              Boss("53",4,3,"Goblin.png"),
              Boss("54",4,4,"Goblin.png"),
              Boss("55",4,5,"Goblin.png")]


}
