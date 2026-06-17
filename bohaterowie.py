import random
import pygame
class Bohater:
    def __init__(self,inteligencja,sila,zrecznosc,hp,nazwa_pliku):
        """ funkcja tworzy postac i ustawia jej podstawowe wlasnosci i charaksterystyki """
    
        self.inteligencja = inteligencja
        self.sila=sila
        self.zrecznosc = zrecznosc

        self.max_hp = hp
        self.aktualne_hp = hp

        self.punkty_umiejetnosci = 0

        self.plik_grafiki = nazwa_pliku
        self.grafika = None

    def otrzymywane_obrazenia(self,obrazenia):
        """ zmniejsza aktualne punkty zdrowia postaci o otrzymane obrazenia oraz ogranicza je tak aby nie spadly ponizej zera"""
        self.aktualne_hp = max(0, int(self.aktualne_hp - obrazenia))

    def atakuj(self, przeciwnik):
        """prowadzi atak na przeciwnika, obliczajac ilosc zadanych obrazen i kierujac je na cel"""
        obrazenia = self.oblicz_obrazenia()
        przeciwnik.otrzymywane_obrazenia(obrazenia)
    
    def czy_zyje(self):
        """sprawdza czy bohater nadal zyje, czy jego hp(punkty zycia)>0, zwraca true or false"""
        return self.aktualne_hp>0
    
    def rysuj(self,screen,x,y):
        """laduje grafike z pliku, skaluje ja i rysuje na oknie gry w okreslonych wspolrzednych x,y"""
        if self.grafika == None:
            self.grafika = pygame.image.load(f"grafiki/{self.plik_grafiki}").convert_alpha()
            docelowy_rozmiar = (250, 250)
            self.grafika = pygame.transform.scale(self.grafika, docelowy_rozmiar)
            self.grafika.set_colorkey((255, 255, 255))
        screen.blit(self.grafika,(x,y))
class Mag(Bohater):
    def __init__(self,inteligencja, sila, zrecznosc, hp, nazwa_pliku):
            """tworzy klase Maga, dostaje wlasnosci z klasy bohaterow """
        super().__init__(inteligencja, sila, zrecznosc, hp, nazwa_pliku)
        
    def oblicz_obrazenia(self):
        """oblicza obrazenia zadawane przez Maga na podstawie jego inteligencji i wylosowanego mnoznika"""
        mnoznik_obrazen = random.uniform(1.8,2.2)
        obrazenia = int(mnoznik_obrazen*self.inteligencja)
        return obrazenia

class Wojownik(Bohater):
    def __init__(self, inteligencja, sila, zrecznosc, hp, nazwa_pliku):
        """tworzy klase Wojownika dostaje wlasnosci z klasy Bohatera"""
        super().__init__(inteligencja, sila, zrecznosc, hp, nazwa_pliku)

    def oblicz_obrazenia(self):
        """oblicza obrazenia zadawane przez wojownika na podstawie jego sily z bonusem 1,5 i wylosowenego mnoznika"""
        mnoznik_obrazen = random.uniform(1.2,1.4)
        obrazenia = int(mnoznik_obrazen*self.sila*1.5)
        return obrazenia

class Lucznik(Bohater):
    def __init__(self, inteligencja, sila, zrecznosc, hp, nazwa_pliku):
        """tworzy klase Lucznika dostaje wlasnosci z klasy bohatera"""
        super().__init__(inteligencja, sila, zrecznosc, hp, nazwa_pliku)

    def oblicz_obrazenia(self):
        """oblicza obrazenia zadawane przez Lucznika na podstawie jego zrecznosci ze stalym bonus 1,3 oraz wylosowanego mnoznika"""
        mnoznik_obrazen = random.uniform(1.0,1.8)
        obrazenia = int(mnoznik_obrazen*self.zrecznosc*1.3)
        return obrazenia
