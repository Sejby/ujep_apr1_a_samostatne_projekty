# Napiš funkci, která porovná dva řetězce a zjistí zda jsou anagramem.


"""
from typing import List

retezec1 = input("Zadej první řetězec")
retezec2 = input("Zadej druhý řetězec")
pole1 = []
pole2 = []

def zjistiAnagram(retezec1: str, retezec2: str, pole1: List, pole2: List) -> bool:
    for pismeno in retezec1:
        pole1 += pismeno
    pole1.sort()

    for pismeno2 in retezec2:
        pole2 += pismeno2
    pole2.sort()

    if pole1 == pole2 and len(pole1) == len(pole2):
        return True
    else:
        return False

print(zjistiAnagram(retezec1=retezec1, retezec2=retezec2, pole1=pole1, pole2=pole2))

"""

# Napiš funkci, která vygeneruje matici o zadaných rozměrech s čísly od 1-255
from typing import List
import random




def vygenerujMatici() -> List:
    sirka = int(input("Zadejte šířku"))
    vyska = int(input("Zadejte výšku"))
    matice = []
    for i in range(sirka):
        radek = []
        for j in range(vyska):
            radek.append(random.randint(1,255))
        matice.append(radek)

    for radek in matice:
        print(radek)
    
    return matice




# Napiš funkci, která z matice vygeneruje obrázek
from matplotlib import pyplot as plt

def vykresli_obrazek_z_matice():
    plt.imshow(vygenerujMatici(),norm=None, cmap="gray")
    plt.show()

vykresli_obrazek_z_matice()




# Napište funkci, která požádá uživatele o heslo a vrátí ho, pouze pokud heslo obsahuje alespoň 1 velké písmeno, 4 malé písmeno a alespoň 1 číslo. 
# Pokud heslo neobsahuje tyto znaky, pak žádá o zadání hesla ještě 2x, jinak vypíše chybu printem a vrátí None.
""" from string import ascii_uppercase, ascii_lowercase

pokus = 0

def kontrolaHesla(pokus: int) -> None:
    pokus += 1
    velkePismeno = False
    cislo = False
    citacMalychPismen = 0
    heslo = input("Zadej heslo")
    for pismeno in heslo:
        if pismeno in ascii_uppercase:
            velkePismeno = True
        if pismeno in ascii_lowercase:
            citacMalychPismen += 1
        if pismeno.isdecimal():
            cislo = True

    if velkePismeno == True and cislo == True and citacMalychPismen >= 4:
        print("Úspěšně přihlášen!")
    elif pokus < 3:
            print(f"Špatně zadané heslo, máš {pokus}/3 pokusů za sebou!")
            kontrolaHesla(pokus=pokus)
    else:
         print("Chyba")
         return None

kontrolaHesla(pokus=pokus)
    
 """

# Spojení seznamů

# Napište funkci, do které vložíte dva seznamy a funkce vám vrátí seznam složený ze dvou řetězců na přeskáčku.

# př.: spoj([1,2,3],["a","b","c"]) -> [1,"a",2,"b",3,"c"]
"""
from typing import List

cisla = [1,2,3]
pismena = ["a","b","c"]
vysledek = []

def spoj(cisla: List, pismena: List, vysledek: List)-> List:
    vysledek = []
    for prvek1, prvek2 in zip(cisla, pismena):
        vysledek.extend([prvek1, prvek2])
    return vysledek

print(spoj(cisla=cisla, pismena=pismena, vysledek=vysledek))
        
"""

# Promíchání písmenek

# Napište funkci, do které vložíte seznam písmenek a funkce vrátí nový seznam, 
# kde budou tato písmenka náhodně rozmíchaná.

"""
import random

seznam = input("Zadej seznam")

def zamichejPismenka(seznam: str) -> str:
    pom = list(seznam)
    random.shuffle(pom)
    vysledek = "".join(pom)
    return vysledek

print(zamichejPismenka(seznam=seznam))
"""
"""
import math

a = int(input("Zadej a kvadratické rovnice:"))
b = int(input("Zadej b kvadratické rovnice:"))
c = int(input("Zadej c kvadratické rovnice:"))

def vypoctiDiskriminant(a: int, b: int, c: int)->int:
    disksriminant = (b**2)-(4*a*c)
    return disksriminant

def spocitej(a: int, b: int, c: int)->int:
    diskriminant = vypoctiDiskriminant(a=a, b=b,c=c)
    x1 = (-b + math.sqrt(diskriminant)) / (2*a)
    x2 = (-b - math.sqrt(diskriminant)) / (2*a)
    return x1,x2

print(spocitej(a=a,b=b,c=c))

"""

# HW7.3: Porovnání frekvence slov dvou textů

# Napište proceduru, která přijme text od uživatele a vrátí seznam slov s počtem výskytů slov v procentech. 
# Tato procedura bude volána z jiné procedury, která přijme 2 texty a vypíše na obrazovku
#  v hezké podobě informace o shodnosti těchto dvou textů (jaké informace to budou je na vás).
"""
from collections import Counter

def prijmi():
    text1 = input("Zadej první text")
    text2 = input("Zadej druhý text")
    return (text1,text2)

def vypis()->str:
    texty = prijmi()
    pocet_shodnych_slov = 0
    for slovo in (texty[0].split(" ")):
        pocet_shodnych_slov += "".join(texty[1]).count(slovo)
    return print(f"Počet shodných slov:{pocet_shodnych_slov}")

vypis()

"""

#Brownovský pohyb

#Napište program strukturovaným paradigmatem, který bude představovat brownovský pohyb jedné částice v prostoru. 
# Realizace ja zcela na vás.
"""

import random
from matplotlib import pyplot as plt

def pripravPole():
    pole = []
    for idx in range(1,50):
        #mělo by tady být deltax,deltay
        x = random.randint(1,50)
        y = random.randint(1,50)
        pole.append((x,y))
    return pole

def nakresliGraf():
    pole = pripravPole()

    plt.xlabel('x')
    plt.ylabel('y')

    x, y = zip(*pole)
    plt.plot(x, y, "ro-")
    plt.show()

nakresliGraf()
"""
