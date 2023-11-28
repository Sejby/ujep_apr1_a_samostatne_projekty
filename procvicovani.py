# Napište funkci, do které vložíte počáteční a konečný prvek z číselné řady a program vám vrátí všechna lichá čísla z této řady.

"""
min = int(input("zadej minimum"))
max = int(input("zadej maximum"))

rada = []


def vratLichaCisla(min: int, max: int) -> list:
    for cislo in range(min, max):
        if not cislo%2 == 0:
            rada.append(cislo)
        else:
            continue
    return rada

print(vratLichaCisla(min=min, max=max))

"""

# Napište proceduru, která přijme seznam hodnot na ose y (řady) a k tomu popisky osy x. Následně vykreslí do jednoho grafu v knihovně matplotlib data na obrazovku. 
# Tím budete mít připravenou proceduru jako náhražku Excelu.

"""
osa_y = []
osa_X = []

import matplotlib.pyplot as plt

def vykresli_graf(kategorie: list, rady: list, nazev: str, 
                  nazev_osy_x: str, nazev_osy_y: str, styl_rad: list) -> None:
    plt.title(nazev)
    plt.xlabel(nazev_osy_x)
    plt.ylabel(nazev_osy_y)
    for irada, rada in enumerate(rady):
        plt.plot(kategorie, rada, styl_rad[irada])
    plt.show()

rady = [
    [5, 6, 3, 1, 0],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
]    
kategorie = ["Po", "Ut", "St", "Ct", "Pa"]
styly = ["ro", "b-", "g.-"]
vykresli_graf(
    kategorie = kategorie, 
    rady = rady,
    nazev = "Graficek",
    nazev_osy_x = "dny", 
    nazev_osy_y = "nejaka cisla",
    styl_rad = styly
)

"""

"""
slova = ('Honza', 'Petr', 'Tomáš')

znamky = []

for student in slova:
    znamky.append([(student), (1)])
    print(znamky)
    
"""

"""

# Napište funkci, do které vložíte řetězec a znak a vrátí se vám počet výskytů tohoto znaku v řetězci.

from collections import Counter

retezec = input("Zadej retezec")
znak = input("zadej znak, který chceš spočítat")

vysledek = retezec.count(znak)
print(f"Znak se nachází tolikrát ve slově: {vysledek}")

"""

#Funkce, která vrátí první prvek v poli a poslední:

"""
def first_and_last_elements(input_list):
    if len(input_list) == 0:
        return None, None
    else:
        return input_list[0], input_list[-1]

my_list = [1, 2, 3, 4, 5]
first, last = first_and_last_elements(my_list)
print(f"První prvek: {first}, Poslední prvek: {last}")

"""


# Funkce pro zjištění prvočísel

"""

from typing import List

cisla = [1,25,4,8,77,999,1000]
prvocisla = []

def zjistiPrvocislo(cisla : List) -> List:
    for cislo in cisla:
        if not cislo % 2 == 0:
            prvocisla.append(cislo)
    print(prvocisla)            
    return prvocisla
    
    
zjistiPrvocislo(cisla=cisla)

"""

# Šifrování a dešifrování

"""
from string import ascii_lowercase

op = input("Chceš šifrovat nebo dešifrovat? S/D")

def zasifruj(retezec: str, posunuti: int) -> str:
    vysledek = ""
    for char in retezec.lower():
        idx_ascii = ascii_lowercase.index(char)
        vysledek += ascii_lowercase[idx_ascii+posunuti]
    print(vysledek)
    return vysledek

def odsifruj(retezec: str, posunuti: int) -> str:
    vysledek = ""
    for char in retezec.lower():
        idx_ascii = ascii_lowercase.index(char)
        vysledek += ascii_lowercase[idx_ascii+posunuti]
    print(vysledek)
    return vysledek

if op == "S":
    posunuti = int(input("Zadejte o kolik chcete šifru posunovat"))
    retezec = input("Zadejte slovo/řetězec, který chcete šifrovat")
    zasifruj(retezec=retezec, posunuti=posunuti)
elif op == "D":
    posunuti_odsifra = int(input("Zadejte o kolik chcete šifru posunovat"))
    retezec_odsifra = input("Zadejte slovo/řetězec, který chcete odšifrovat")
    odsifruj(retezec=retezec_odsifra, posunuti=posunuti_odsifra)
    
"""

# Zpracování seznamů:

# Vytvořte funkci, která najde největší prvek v seznamu čísel.
# Implementujte funkci, která seřadí seznam čísel od nejmenšího po největší.

"""
from typing import List

cisla = [25, 3, 9, 1209, 999, 12955, 99999, 0]

def nejvetsiPrvek(pole: List) -> List:
    pole.sort()
    print(f"Největší prvek: {pole[-1]}")
    return pole

print(nejvetsiPrvek(pole=cisla))

"""

# Práce s řetězci:

# Napište funkci, která ověří, zda zadaný řetězec je palindrom (čte se stejně zleva i zprava).
# Vytvořte funkci, která nahradí ve zadaném textu všechny výskyty určitého slova jiným slovem.

"""

retezec = input("Zadej slovo, u kterého chceš zjistit, zda je palindrom")


def zjistiPalindrom(retezec: str) -> bool:
    pom = list(retezec)
    pom.reverse()
    if "".join(pom) == retezec:
        print("Je to palindrom")
        return True
    else:
        print("Není to palindrom")
        return False

print(zjistiPalindrom(retezec=retezec))

"""

#Zpracování textu:

# Napište funkci, která převede text na malá písmena a odstraní z něj diakritiku.
# Vytvořte funkci, která spočítá počet slov v textu a vrátí je.


"""

def spocitej_slova(text: str) -> int:
    slova = text.split()
    print(slova)
    
    pocet_slov = len(slova)
    return pocet_slov

vstupni_text = "Toto je příklad textu s několika slovy."
pocet_slov = spocitej_slova(vstupni_text)
print(f"Počet slov: {pocet_slov}") 

"""
    

