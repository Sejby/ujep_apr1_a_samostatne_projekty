''' import math
teleso = input("Zadejte těleso, u kterého chcete spočítat objem: (kvadr, krychle, koule)")
delka = int(input("Zadejte délku v cm:"))
sirka = int(input("Zadejte šířku v cm:"))
vyska = int(input("Zadejte výšku v cm:"))

rozmery = {
    delka: delka,
    sirka: sirka,
    vyska: vyska,
}


def objem(rozmery, teleso):
    match teleso:
        case "kvadr":
            objem = rozmery[delka] * rozmery[sirka] * rozmery[vyska]
            return objem
        case "krychle":
            objem = rozmery[delka]**3
            return objem
        case "koule":
            r = rozmery[delka] / 2
            objem = (4/3)*math.pi*r**3
            return objem
        
        
        

print(f"Objem {teleso} je: {objem(rozmery, teleso)} cm3")

 '''
 
''' vstup = input("Zadej slovo")

def velka(vstup):
    return vstup.upper()

print(f"{velka(vstup)}") '''

"""

retezec = input("Zadej slovo")
listik = list(retezec)
pismena = list


def kazdeDruhe(retezec : str):
    for idx in range(len(listik)):
        if idx <= len(listik):
            kazdeDruhePismeno = pismena.append(listik[idx+2])
        else:
            break

print(f"{kazdeDruhe(retezec)} {pismena}")

"""

#1  Napište funkci, do které vložité seznam čísel a ona vrátí čísla dělitelná bezezbytku 7mi
#2 Napište funkci, do které vložíte seznam čísel a ona vrátí příslušná písmena abecedy
#3 Napište fci, která vygeneruje matici náhodných čísel od 0 do 255 o zadané šířce a výšce
#4 Napište fci, která zobrazí matici náhodných čísel jako obrázek
#5 Napište f, do které vložíte dva řetězce a ona zjistí zda je anagram (stejný počet písmen)

#Zápočtový test - obdovné úlohy jako výše

  # napište funkci aby vrátila tohle a tohle
    #seznam ntic, seznam množin, funkce musí vrátit tohle a tohle


"""
cisla = [1,7,8,2,5,6,14,21]
delitelna_cisla = []


def delitelna_sedmi(seznam):
    for cislo in seznam:
        if cislo % 7 == 0:
            delitelna_cisla.append(cislo)
        else:
            break
        return delitelna_cisla

print(delitelna_sedmi(cisla))


"""


"""

from typing import List, Tuple
from string import ascii_lowercase

seznam_cisel = [5,6,7,2,0,10]
pismenka = []


def prislusnaPismena(indexy: List[int]) -> List[str]:
    for index in indexy:
        if not index > len(ascii_lowercase):
            pismenka.append(ascii_lowercase[index])
    return pismenka

print(prislusnaPismena(seznam_cisel))

"""


"""
import random

sirka = int(input("Zadejte šírku matice"))
vyska = int(input("zadejte výšku matice"))
meze = (0,255)

matice = []
def nahodna_matice(sirka : int, vyska : int):
    for iradek in range(vyska):
        radek = []
        for isloupec in range(sirka):
            radek.append(random.randint(meze[0], meze[1]))
        matice.append(radek)
    return matice

import matplotlib.pyplot as plt
from typing import List, Tuple

def vykresliObrazek(matice: List[list[int]]) -> None:
    plt.imshow(matice, cmap="gray")
    
vykresliObrazek(nahodna_matice(100, 100))

"""
"""

from string import ascii_lowercase

retezec1 = input("zadej slovo")
retezec2 = input("zadej slovo2")
pismenka1 = list(retezec1)
pismenka2 = list(retezec2)


def zjistiAnagram(retezec1: str, retezec2: str):
    pismenka1.append(retezec1.split())
    pismenka2.append(retezec2.split())    
    
    for idx in range(len(pismenka1)):
        counter1 = pismenka1.count(ascii_lowercase)
    for idx in range(len(pismenka2)):
        counter2 = pismenka2.count(ascii_lowercase)
        
    if counter1 == counter2:
        print("Je to anagram")
    else:
        print("Není to anagram")
        
        
print(zjistiAnagram(retezec1=retezec1, retezec2=retezec2))


from collections import Counter

def jsou_anagram(veta1: str, veta2: str) -> bool:
    return Counter(veta1) == Counter(veta2)
    
"""
"""
#Napište kód pro člověče nezlob se s jednou figurkou o jednom hráči
#sem psát jednotilivé funkce

import random


policko = 0

def hra():
    while not akceptance(policko):
        hoditKostku()
    #dostat se z počátečního domečku na 6ku
    #hodit kostkou, pokud padne 6, tak házíme znovu
    #průběžné výpisy, kde jsem
    #akceptance do cílového domečku na správný hod kostkou
    #napište
    
  
    

def vypisPozici(policko: int, hod_kostkou: int):
    policko = policko + hod_kostkou
    print(f"Nacházíte se na {policko} políčku")
    akceptance(policko=policko)
    return policko


def hoditKostku():
    input("Zmáčkni ENTER pro hod kostkou")
    kostka = random.randint(1,6)
    if kostka == 6:
        hoditKostku()
        print("Házíš znova!")
    else:
        print(f"Padlo číslo {kostka}")
        vypisPozici(policko, kostka)
        return kostka
     
def akceptance(policko):
    if policko > 6:
        print("Jste v cíli!")
        return True
    else:
        print("Házej znovu!")
        return False
        
        
    
hra()

"""

