import pygame
import sys
from bohaterowie import Mag, Wojownik, Lucznik
from bossowie import poziomy_trudnosci

class Przycisk():
    def __init__(self,x,y,szerokosc,wysokosc,napis):
        self.rect = pygame.Rect(x,y,szerokosc,wysokosc)
        self.kolor_bazowy = (70,70,70)
        self.kolor_hover = (30,30,30)
        self.kolor_tekst = (200,200,200)
        self.obecny_kolor = self.kolor_bazowy
        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 16)
        self.tekst_surface = self.font.render(napis,1,self.kolor_tekst)
        self.tekst_rect = self.tekst_surface.get_rect(center = self.rect.center)
    def update(self,mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.obecny_kolor = self.kolor_hover
        else:
            self.obecny_kolor = self.kolor_bazowy
    def rysowanie(self,surface,alpha=255):
        # pygame.draw.rect(surface,self.obecny_kolor,self.rect)
        # surface.blit(self.tekst_surface,self.tekst_rect)
        przycisk_surface = pygame.Surface((self.rect.width, self.rect.height))
        przycisk_surface.set_alpha(alpha)
        przycisk_surface.fill(self.obecny_kolor)
        surface.blit(przycisk_surface, (self.rect.x, self.rect.y))
        surface.blit(self.tekst_surface, self.tekst_rect)
    def czy_kliknieto(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False
class Gra:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,750))
        pygame.display.set_caption("Bossrush")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 14)

        self.stan_wybor_postaci = "WYBOR POSTACI"
        self.stan_mapa_glowna = "MENU GLOWNA"
        self.stan_wybor_bossa = "WYBOR BOSSA"
        self.stan_walka = "WALKA"
        self.stan_ulepszanie = "ULEPSZANIE"
        self.stan_koniec_gry = "KONIEC GRY"
        self.aktualny_stan = self.stan_wybor_postaci

        self.gracz = None
        self.aktywny_akt = None
        self.aktywny_boss = None

        tlo_akt_1 = pygame.image.load("grafiki/akt_1.png").convert_alpha()
        tlo_akt_1 = pygame.transform.scale(tlo_akt_1,(1000,750))
        tlo_akt_2 = pygame.image.load("grafiki/akt_2.png").convert_alpha()
        tlo_akt_2 = pygame.transform.scale(tlo_akt_2,(1000,750))
        tlo_akt_3 = pygame.image.load("grafiki/akt_3.png").convert_alpha()
        tlo_akt_3 = pygame.transform.scale(tlo_akt_3,(1000,750))
        tlo_akt_4 = pygame.image.load("grafiki/akt_4.png").convert_alpha()
        tlo_akt_4 = pygame.transform.scale(tlo_akt_4,(1000,750))
        self.tla_aktow = {
            "Latwy": tlo_akt_1,   
            "Sredni": tlo_akt_2,     
            "Trudny": tlo_akt_3,  
            "Epicki": tlo_akt_4     
        }

        self.przycisk_Mag = Przycisk(100, 320, 200, 100, "Mag")
        self.przycisk_Wojownik = Przycisk(400, 320, 200, 100, "Wojownik")
        self.przycisk_Lucznik = Przycisk(700, 320, 200, 100, "Lucznik")

        self.przycisk_Akt1 = Przycisk(140,120,220,80,"Akt_1")
        self.przycisk_Akt2 = Przycisk(640,120,220,80,"Akt_2")
        self.przycisk_Akt3 = Przycisk(140,600,220,80,"Akt_3")
        self.przycisk_Akt4 = Przycisk(640,600,220,80,"Akt_4")
        self.przycisk_menu_ulepszen = Przycisk(370,355,260,90,"Menu Ulepszen")

        self.przycisk_ulep_sila = Przycisk(220,120,80,80,"+")
        self.przycisk_ulep_int = Przycisk(840,120,80,80,"+")
        self.przycisk_ulep_zr = Przycisk(220,600,80,80,"+")
        self.przycisk_ulep_hp = Przycisk(840,600,80,80,"+")
        self.przycisk_mapa = Przycisk(10,10,260,90,"Powrot do mapy")

        self.przyciski_bossow=[]

        self.przycisk_walka = Przycisk(400, 550, 200, 80, "ATAKUJ")

        self.przycisk_odrodzenie = Przycisk(370, 450, 260, 60, "Odrodzenie")

        self.log_gracz = "Wybierz akcje!"
        self.log_boss = ""

        self.mapa_tlo = pygame.image.load(f"grafiki/mapka.png").convert_alpha()
        self.mapa_tlo = pygame.transform.scale(self.mapa_tlo, (1000, 700))



    def start_gry(self):
        while True:
            self.obsluga_eventow()
            self.rysuj_gre()
            self.clock.tick(30)

    def obsluga_eventow(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if self.aktualny_stan == self.stan_wybor_postaci:
                self.logika_wybor_bohaterow(event)
            elif self.aktualny_stan == self.stan_mapa_glowna:
                self.logika_mapa_glowna(event)
            elif self.aktualny_stan == self.stan_ulepszanie:
                self.logika_ulepszanie(event)
            elif self.aktualny_stan == self.stan_wybor_bossa:
                self.logika_wybor_bossa(event)
            elif self.aktualny_stan == self.stan_walka:
                self.logika_walka(event)
            elif self.aktualny_stan == self.stan_koniec_gry:
                self.logika_koniec_gry(event)
    
    def logika_koniec_gry(self,event):
        if self.przycisk_odrodzenie.czy_kliknieto(event):
            self.gracz.aktualne_hp=self.gracz.max_hp
            self.aktualny_stan = self.stan_mapa_glowna
    
    def logika_wybor_bohaterow(self,event):
        if self.przycisk_Mag.czy_kliknieto(event):
            self.gracz = Mag(inteligencja=18, sila=3, zrecznosc=4, hp=90, nazwa_pliku="mag.png")
            self.aktualny_stan = self.stan_mapa_glowna
        elif self.przycisk_Wojownik.czy_kliknieto(event):
            self.gracz = Wojownik(inteligencja=5, sila=15, zrecznosc=4, hp=150, nazwa_pliku="wojownik.png")
            self.aktualny_stan = self.stan_mapa_glowna
        elif self.przycisk_Lucznik.czy_kliknieto(event):
            self.gracz = Lucznik(inteligencja=4, sila=4, zrecznosc=16, hp=120, nazwa_pliku="lucznik.png")
            self.aktualny_stan = self.stan_mapa_glowna
    
    def logika_mapa_glowna(self,event):
        wybrany_poziom = None
        if self.przycisk_Akt1.czy_kliknieto(event):
            wybrany_poziom = "Latwy"
            # self.aktualny_stan = self.stan_akt1
        elif self.przycisk_Akt2.czy_kliknieto(event):
            wybrany_poziom = "Sredni"
            # self.aktualny_stan = self.stan_akt2
        elif self.przycisk_Akt3.czy_kliknieto(event):
            wybrany_poziom = "Trudny"
            # self.aktualny_stan = self.stan_akt3
        elif self.przycisk_Akt4.czy_kliknieto(event):
            wybrany_poziom = "Epicki"
            # self.aktualny_stan = self.stan_akt4
        
        if wybrany_poziom:
            self.aktywny_akt = wybrany_poziom
            self.aktualny_stan = self.stan_wybor_bossa

            self.przyciski_bossow.clear()

            for i in range(5):
                boss = poziomy_trudnosci[self.aktywny_akt][i]
                nowy_przycisk = Przycisk(370, 100 + (i * 90), 260, 60, boss.nazwa)
                self.przyciski_bossow.append(nowy_przycisk)

        elif self.przycisk_menu_ulepszen.czy_kliknieto(event):
            self.aktualny_stan = self.stan_ulepszanie

    def logika_ulepszanie(self,event):
        if self.gracz.punkty_umiejetnosci>0:
            if self.przycisk_ulep_sila.czy_kliknieto(event):
                self.gracz.sila += 1
                self.gracz.punkty_umiejetnosci -= 1
            elif self.przycisk_ulep_int.czy_kliknieto(event):
                self.gracz.inteligencja += 1
                self.gracz.punkty_umiejetnosci -= 1
            elif self.przycisk_ulep_zr.czy_kliknieto(event):
                self.gracz.zrecznosc += 1
                self.gracz.punkty_umiejetnosci -= 1
            elif self.przycisk_ulep_hp.czy_kliknieto(event):
                if isinstance(self.gracz, Wojownik):
                    bonus_hp = 3
                elif isinstance(self.gracz, Lucznik):
                    bonus_hp = 2 
                elif isinstance(self.gracz, Mag):
                    bonus_hp = 1
                self.gracz.max_hp += bonus_hp
                self.gracz.aktualne_hp += bonus_hp
                self.gracz.punkty_umiejetnosci -= 1
        if self.przycisk_mapa.czy_kliknieto(event):
            self.aktualny_stan = self.stan_mapa_glowna

    def logika_wybor_bossa(self,event):
        if self.przycisk_mapa.czy_kliknieto(event):
            self.aktualny_stan = self.stan_mapa_glowna
        
        for i, przycisk in enumerate(self.przyciski_bossow):
            if przycisk.czy_kliknieto(event):
                self.aktywny_boss = poziomy_trudnosci[self.aktywny_akt][i]
                self.aktywny_boss.aktualne_hp = self.aktywny_boss.max_hp

                self.log_gracza = f"Walczysz z: {self.aktywny_boss.nazwa}"
                self.log_bossa = "Przygotuj sie!"

                self.aktualny_stan = self.stan_walka
                return
            
    def logika_walka(self,event):
        if self.przycisk_walka.czy_kliknieto(event):
            hp_bossa_przed = self.aktywny_boss.aktualne_hp
            self.gracz.atakuj(self.aktywny_boss)
            obr_gracza = hp_bossa_przed - self.aktywny_boss.aktualne_hp
            self.log_gracza = f"Zadales {obr_gracza} obrazen"
            if self.aktywny_boss.czy_zyje():
                hp_gracza_przed = self.gracz.aktualne_hp
                self.aktywny_boss.atak(self.gracz)
                obr_bossa = hp_gracza_przed - self.gracz.aktualne_hp
                self.log_bossa = f"Boss zadal {obr_bossa} obrazen"
            else:
                self.log_bossa = "Boss zostal pokonany!"
            if not self.aktywny_boss.czy_zyje():
                self.gracz.punkty_umiejetnosci += 3
                self.gracz.aktualne_hp=self.gracz.max_hp
                self.aktualny_stan = self.stan_mapa_glowna
            if not self.gracz.czy_zyje():
                self.aktualny_stan = self.stan_koniec_gry

    def rysuj_gre(self):
        self.screen.fill((30, 30, 30))
        if self.aktualny_stan == self.stan_wybor_postaci:
            self.przycisk_Mag.update(pygame.mouse.get_pos())
            self.przycisk_Mag.rysowanie(self.screen)
            self.przycisk_Wojownik.update(pygame.mouse.get_pos())
            self.przycisk_Wojownik.rysowanie(self.screen)
            self.przycisk_Lucznik.update(pygame.mouse.get_pos())
            self.przycisk_Lucznik.rysowanie(self.screen)
        if self.aktualny_stan == self.stan_mapa_glowna:
            self.screen.blit(self.mapa_tlo, (0, 0))
            self.przycisk_menu_ulepszen.rysowanie(self.screen,128)
            self.przycisk_menu_ulepszen.update(pygame.mouse.get_pos())
            self.przycisk_Akt1.rysowanie(self.screen,128)
            self.przycisk_Akt1.update(pygame.mouse.get_pos())
            self.przycisk_Akt2.rysowanie(self.screen,128)
            self.przycisk_Akt2.update(pygame.mouse.get_pos())
            self.przycisk_Akt3.rysowanie(self.screen,128)
            self.przycisk_Akt3.update(pygame.mouse.get_pos())
            self.przycisk_Akt4.rysowanie(self.screen,128)
            self.przycisk_Akt4.update(pygame.mouse.get_pos())
        if self.aktualny_stan == self.stan_ulepszanie:
            self.przycisk_mapa.rysowanie(self.screen)
            self.przycisk_mapa.update(pygame.mouse.get_pos())
            self.przycisk_ulep_sila.rysowanie(self.screen)
            self.przycisk_ulep_sila.update(pygame.mouse.get_pos())
            self.przycisk_ulep_int.rysowanie(self.screen)
            self.przycisk_ulep_int.update(pygame.mouse.get_pos())
            self.przycisk_ulep_zr.rysowanie(self.screen)
            self.przycisk_ulep_zr.update(pygame.mouse.get_pos())
            self.przycisk_ulep_hp.rysowanie(self.screen)
            self.przycisk_ulep_hp.update(pygame.mouse.get_pos())

            tekst_pkt = self.font.render(f"dostepne punkty umiejetnosci: {self.gracz.punkty_umiejetnosci}",1,(255,215,0))
            tekst_sila = self.font.render(f"sila: {self.gracz.sila}",1,(255,255,255))
            tekst_int = self.font.render(f"inteligencja: {self.gracz.inteligencja}",1,(255,255,255))
            tekst_zr = self.font.render(f"zrecznosc: {self.gracz.zrecznosc}",1,(255,255,255))
            tekst_hp = self.font.render(f"hp: {self.gracz.max_hp}",1,(255,255,255))

            self.screen.blit(tekst_pkt,(370,20))
            self.screen.blit(tekst_sila,(90,155,220,80))
            self.screen.blit(tekst_int,(600,155,220,80))
            self.screen.blit(tekst_zr,(50,635,220,80))
            self.screen.blit(tekst_hp,(720,635,220,80))
        if self.aktualny_stan == self.stan_wybor_bossa:
            obraz_tlo = self.tla_aktow.get(self.aktywny_akt)
            # kolor_tla = self.tla_aktow.get(self.aktywny_akt)
            self.screen.blit(obraz_tlo,(0,0))
            # self.screen.fill(kolor_tla)

            self.przycisk_mapa.rysowanie(self.screen)
            self.przycisk_mapa.update(pygame.mouse.get_pos())

            for przycisk in self.przyciski_bossow:
                przycisk.update(pygame.mouse.get_pos())
                przycisk.rysowanie(self.screen)
        
        if self.aktualny_stan == self.stan_walka:
            obraz_tlo = self.tla_aktow.get(self.aktywny_akt)
            self.screen.blit(obraz_tlo,(0,0))
            self.przycisk_walka.update(pygame.mouse.get_pos())
            self.przycisk_walka.rysowanie(self.screen)
            tekst_gracz = self.font.render(f"Gracz HP: {self.gracz.aktualne_hp}/{self.gracz.max_hp}", True, (0, 255, 0))
            tekst_boss = self.font.render(f"Boss HP: {self.aktywny_boss.aktualne_hp}/{self.aktywny_boss.max_hp}", True, (255, 0, 0))
            self.screen.blit(tekst_gracz, (100, 100))
            self.screen.blit(tekst_boss, (600, 100))
            log_gr = self.font.render(self.log_gracza, 1, (255, 255, 100)) 
            log_bo = self.font.render(self.log_bossa, 1, (255, 150, 150))  
            self.screen.blit(log_gr, (350, 300))
            self.screen.blit(log_bo, (350, 350))

            self.aktywny_boss.rysuj(self.screen, 700, 350)
            self.gracz.rysuj(self.screen, 50, 350)

        if self.aktualny_stan == self.stan_koniec_gry:
            self.screen.fill((50, 0, 0))
            tekst = self.font.render("zginales w walce...", 1, (255, 50, 50))
            self.screen.blit(tekst, (350, 300))
            
            self.przycisk_odrodzenie.update(pygame.mouse.get_pos())
            self.przycisk_odrodzenie.rysowanie(self.screen)


        pygame.display.flip()

if __name__ == "__main__":
    Gra().start_gry()