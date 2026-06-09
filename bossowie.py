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
            docelowy_rozmiar = (250, 250)
            self.grafika = pygame.transform.scale(self.grafika, docelowy_rozmiar)
            self.grafika.set_colorkey((255, 255, 255))
        screen.blit(self.grafika, (x, y))
poziomy_trudnosci = {
    "Latwy": [Boss("Goblin",1,1,"Goblin.png"),
              Boss("Oko",1,2,"oko.png"),
              Boss("Grzyb",1,3,"grzyb.png"),
              Boss("Robok",1,4,"wyrmling.png"),
              Boss("Driada",1,5,"driada.png")],
    "Sredni": [Boss("Szkielet",2,1,"szkielet.png"),
              Boss("Mech Pająk",2,2,"pajak.png"),
              Boss("Cyborg",2,3,"cyborg.png"),
              Boss("Dinożar",2,4,"dizozar.png"),
              Boss("Straznik",2,5,"straznik.png")],
    "Trudny": [Boss("Hagrid",3,1,"lesny.png"),
              Boss("Czarodziej",3,2,"wizard.png"),
              Boss("Alchemik",3,3,"alchemik.png"),
              Boss("Harry Potter",3,4,"fioletowy.png"),
              Boss("Mroczny Czarodziej",3,5,"czardziej_szkielet.png")],
    "Epicki": [Boss("Samuraj",4,1,"samuraj.png"),
              Boss("Pan Lodu",4,2,"mrozny_rycerz.png"),
              Boss("Mroczny rycerz",4,3,"szogun.png"),
              Boss("Nocny Łowca",4,4,"nocny_rycerz.png"),
              Boss("Strażnik Wulkaniczny",4,5,"wulkan_rycerz.png")]


}
