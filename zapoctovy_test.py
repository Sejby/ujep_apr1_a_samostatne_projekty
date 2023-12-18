# 1) Napište funkci, která přijme seznam jmen a pokud začíná slovo na samohlásku, vrátí ho jako počet znaků ve slovu.
# 2) Napište funkci, která přijme seznam čísel, a vrátí ten samý seznam čísel bez duplikátů.
# 3) Napiš funkci, která přijme seznam čísel, a vrátí odpovídající hodnoty v abecedě.

from typing import List
from string import ascii_lowercase


seznam_jmen = ["alena", "pepa", "josef", "emil"]

def vyres_samohlasky(seznam_jmen: List)->List:
    vysledek = []
    for slovo in seznam_jmen:
        if slovo[0] in "aeiouy":
            vysledek.append(len(slovo))
        else:
            vysledek.append(slovo)

    return vysledek



def vrat_bez_duplikatu(seznam_cisel: List)->List:
    seznam_cisel = [1,1,2,3,3]
    vysledek = []
    for cislo in seznam_cisel:
        if not cislo in vysledek and seznam_cisel.count(cislo) >= 2:
            vysledek.append(cislo)
    
    return vysledek

seznam_cisel = [0,1,2,4]

def vrat_hodnoty_abecedy(seznam_cisel: List)->List:
    vysledek = []
    for cislo in seznam_cisel:
        vysledek.append(ascii_lowercase[cislo])    
    return vysledek