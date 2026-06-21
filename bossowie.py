import random
import pygame
from typing import Any, Dict, List


class Boss():
    """Klasa reprezentująca bossa w grze."""

    def __init__(self, nazwa: str, akt: int, poziom: int, nazwa_pliku_grafiki: str) -> None:
        """
        Inicjalizuje bossa.

        Args:
            nazwa: Nazwa bossa.
            akt: Poziom aktualny (wpływa na statystyki).
            poziom: Poziom trudności wewnątrz kategorii.
            nazwa_pliku_grafiki: Nazwa pliku z grafiką.
        """
        self.nazwa: str = nazwa
        self.akt: int = akt
        self.poziom: int = poziom

        self.max_hp: int = int(50 + (self.akt - 1) * 150 + self.poziom * 30 * self.akt)
        self.aktualne_hp: int = self.max_hp
        self.dmg: int = 10 + self.poziom + self.akt * 5

        self.plik_grafiki: str = nazwa_pliku_grafiki
        self.grafika: Any = None

    def otrzymywane_obrazenia(self, obrazenia: float) -> None:
        """Zmniejsza aktualne HP bossa o zadane obrażenia, nie pozwalając spaść poniżej 0."""
        self.aktualne_hp = max(0, int(self.aktualne_hp - obrazenia))

    def czy_zyje(self) -> bool:
        """Sprawdza, czy boss jeszcze żyje (HP > 0)."""
        return self.aktualne_hp > 0

    def atak(self, przeciwnik: 'Boss') -> None:
        """
        Zadaje obrażenia przeciwnikowi z losowym mnożnikiem 1.4-1.5.

        Args:
            przeciwnik: Obiekt bossa, który otrzymuje obrażenia.
        """
        mnoznik_obrazen: float = round(random.uniform(1.4, 1.5), 2)
        obrazenia: float = mnoznik_obrazen * self.dmg
        przeciwnik.otrzymywane_obrazenia(obrazenia)

    def rysuj(self, screen: pygame.Surface, x: int, y: int) -> None:
        """Ładuje i rysuje grafikę bossa na ekranie."""
        if self.grafika is None:
            self.grafika = pygame.image.load(f"grafiki/{self.plik_grafiki}").convert_alpha()
            docelowy_rozmiar: tuple[int, int] = (250, 250)
            self.grafika = pygame.transform.scale(self.grafika, docelowy_rozmiar)
            self.grafika.set_colorkey((255, 255, 255))
        screen.blit(self.grafika, (x, y))


poziomy_trudnosci: Dict[str, List[Boss]] = {
    "Latwy": [Boss("Goblin", 1, 1, "Goblin.png"),
              Boss("Oko", 1, 2, "oko.png"),
              Boss("Grzyb", 1, 3, "grzyb.png"),
              Boss("Robok", 1, 4, "wyrmling.png"),
              Boss("Driada", 1, 5, "driada.png")],
    "Sredni": [Boss("Szkielet", 2, 1, "szkielet.png"),
               Boss("Mech Pająk", 2, 2, "pajak.png"),
               Boss("Cyborg", 2, 3, "cyborg.png"),
               Boss("Dinożar", 2, 4, "dizozar.png"),
               Boss("Straznik", 2, 5, "straznik.png")],
    "Trudny": [Boss("Hagrid", 3, 1, "lesny.png"),
               Boss("Czarodziej", 3, 2, "wizard.png"),
               Boss("Alchemik", 3, 3, "alchemik.png"),
               Boss("Harry Potter", 3, 4, "fioletowy.png"),
               Boss("Mroczny Czarodziej", 3, 5, "czardziej_szkielet.png")],
    "Epicki": [Boss("Samuraj", 4, 1, "samuraj.png"),
               Boss("Pan Lodu", 4, 2, "mrozny_rycerz.png"),
               Boss("Mroczny rycerz", 4, 3, "szogun.png"),
               Boss("Nocny Łowca", 4, 4, "nocny_rycerz.png"),
               Boss("Strażnik Wulkaniczny", 4, 5, "wulkan_rycerz.png")]
}
