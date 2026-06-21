import pytest
from bohaterowie import Mag, Wojownik, Lucznik
from bossowie import Boss

# 1. FIXTURY (Przygotowanie narzędzi)
@pytest.fixture
def wojownik() -> Wojownik:
    return Wojownik(inteligencja=5, sila=10, zrecznosc=4, hp=150, nazwa_pliku="wojownik.png")

@pytest.fixture
def mag() -> Mag:
    return Mag(inteligencja=10, sila=3, zrecznosc=4, hp=90, nazwa_pliku="mag.png")

# 2. TESTY (Sprawdzanie mechanik)
def test_otrzymywanie_obrazen(wojownik: Wojownik) -> None:
    hp_poczatkowe = wojownik.aktualne_hp
    wojownik.otrzymywane_obrazenia(20)
    
    assert wojownik.aktualne_hp == hp_poczatkowe - 20

def test_czy_zyje_i_smierc(wojownik: Wojownik) -> None:
    assert wojownik.czy_zyje() is True
    
    wojownik.otrzymywane_obrazenia(9999) 
    
    assert wojownik.czy_zyje() is False
    assert wojownik.aktualne_hp == 0

def test_awansowanie_statystyk(wojownik: Wojownik) -> None:
    sila_poczatkowa = wojownik.sila
    wojownik.punkty_umiejetnosci = 1
    
    wojownik.sila += 1
    wojownik.punkty_umiejetnosci -= 1
    
    assert wojownik.sila == sila_poczatkowa + 1
    assert wojownik.punkty_umiejetnosci == 0

def test_obrazenia_maga(mag: Mag) -> None:
    obrazenia = mag.oblicz_obrazenia()
    assert 18 <= obrazenia <= 22, f"obrażenia maga {obrazenia} poza zakresem"

def test_skalowanie_hp_bossa() -> None:
    boss_test = Boss(nazwa="boss_test", akt=2, poziom=1, nazwa_pliku_grafiki="test.png")
    assert boss_test.max_hp == 260