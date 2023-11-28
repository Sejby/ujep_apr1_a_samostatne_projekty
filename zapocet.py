# Napište funkci, která vstupuje seznam čísel a má za úkol vrátit čísla dělitelná bezezbytku 7.
# Napište funkci, do které vstoupí seznam čísel a má za úkol vrátit příslušná písmena abecedy k těmto číslům.
# Napište funkci, která má za úkol generovat matici náhodných čísel v určeném rozsahu a zadaných rozměrech.
# Napište funkci, která má za úkol zobrazit matici náhodných čísel jako obrázek.
# Napište funkci, do které vstoupí dva řetězce a má za úkol zjistit, zda jsou tyto řetězce anagramy (tj. obsahují stejný počet písmen).



# Podobné úlohy 

#2 
# Napište funkci, do které vstoupí seznam čísel a má za úkol vrátit jim odpovídající písmena abecedy.

"""

from string import ascii_lowercase
from typing import List

cisla = [1,2,3,4,5,0]
pom = []
vysledek = ""

def vratOdpovidajici(cisla: List) -> List:  
    for cislo in cisla:
        # idk kolik má abeceda písmen??
        if not cislo > 24 and cislo >= 1:
            pom.append(ascii_lowercase[cislo-1])
        else:
            print("Chyba při zadávání")
        vysledek = "".join(pom)
    return vysledek
        
print(vratOdpovidajici(cisla=cisla))

"""


# Napište funkci, která má za úkol generovat matici náhodných čísel v určeném rozsahu a zadaných rozměrech.
"""

import random
import matplotlib.pyplot as plt
from typing import List

def generuj_nahodnou_matici(sirka, vyska):
    matice = []
    
    for i in range(vyska):
        radek = []
        for j in range(sirka):
            radek.append(random.randint(0, 255))
        matice.append(radek)
    
    return matice

sirka = 5
vyska = 3
matice = generuj_nahodnou_matici(sirka, vyska)
for radek in matice:
    print(radek)


def vykresliObrazek(matice: List[list[int]]) -> None:
    plt.imshow(matice, cmap="gray")
    plt.show()
    
vykresliObrazek(generuj_nahodnou_matici(1000,1000))

"""

# Napište funkci, do které vstoupí dva řetězce a má za úkol zjistit, zda jsou tyto řetězce anagramy
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
"""

"""
import math


a = int(input("Zadej číslo a"))
b = int(input("Zadej číslo b"))
c = int(input("Zadej číslo c"))

def Diskriminant(a,b,c):
    D = (b**2)-(4*a*c)
    return D

def vypoctiX(a,b,c):
    D = Diskriminant(a=a,b=b,c=c)
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    return x1,x2


print(vypoctiX(a=a,b=b,c=c))

"""
"""
import matplotlib.pyplot as plt

#tady zacina program
def main():
    t = list(range(76))  #časové stopy (týdny)
    N = 7768662420       #světová populace
    I = 1                #počet nakažených
    R = 0                #počet vyléčených
    S = N - I            #počet nakazitelných
  
    nakazitelni = [S]
    nakazeni = [I]
    vyleceni = [R]

    rychlostSireni = 1.5     #nejaktuálnější basic reproduction rate: https://en.wikipedia.org/wiki/Basic_reproduction_number
    rychlostZotaveni = 0.5  #recovery rate kterej sem si přibližně spočítal (průměrnej denní přirůstek nakažených/průměrnej denní přirůstek vyléčených)

    for i in range(75):
        dS = - rychlostSireni * I * S / N
        dI = rychlostSireni * I * S / N - rychlostZotaveni * I
        dR = rychlostZotaveni * I
        S += dS
        I += dI
        R += dR

        nakazitelni.append(S)
        nakazeni.append(I)
        vyleceni.append(R)

    plt.title("SIR Model of Coronavirus")
    plt.ylabel("World Population")
    plt.xlabel("Time")
    plt.plot(t,nakazitelni,"b-",label = "Susceptible")
    plt.plot(t,nakazeni,"r-",label = "Infected")
    plt.plot(t,vyleceni,"m-",label = "Recovered")
    plt.legend()
    plt.show()


if __name__== "__main__":
    main()
    
"""

"""
from PIL import Image
obrazek = Image.open("habik.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        if prumer > 127:
            obrazek.putpixel((x,y), (r+30, g+30, b+30))
        else:
            obrazek.putpixel((x,y), (r-30, g-30, b-30))
        y += 1
    x += 1
display(obrazek)

"""

#Pořadí písmen

# Napište algoritmus s využitím zip, který převezme seznam čísel a 
# seznam písmen a vrátí seznam dvojic (číslo, písmeno), kde číslo představuje pořadí písmena v abecedě.
# Pro zadání seznamu písmen využijte string.ascii_lowercase a seznam čísel vhodným způsobem vygenerujte na základě velikosti seznamu string.ascii_lowercase.

"""
from string import ascii_lowercase
from typing import List


seznam_cisel = [5,8,1,3,4,10,5,7,15,20,22]
vysledek = []

def poradi(seznam_cisel: List):
    for cislo in seznam_cisel:
        vysledek.append((cislo, ascii_lowercase[cislo-1]))
    return vysledek

print(poradi(seznam_cisel=seznam_cisel))
"""

''' from string import ascii_lowercase
from typing import List

def sifra(retezec: str, posun: int):
    vysledek = []
    list(retezec)
    for pismeno in retezec:
        vysledek.append(ascii_lowercase[ascii_lowercase.index(pismeno)+posun])
    return "".join(vysledek)

def odsifra(retezec: str, posun: int):
    vysledek = []
    list(retezec)
    for pismeno in retezec:
        vysledek.append(ascii_lowercase[ascii_lowercase.index(pismeno)-posun])
    return "".join(vysledek)

if input("Chceš šifrovat nebo odšifrovat? S/O") == "S":
    retezec = input("Zadej, co chceš zašifrovat")
    posun = int(input("Zadej o kolik chceš posunout"))
    sifra(retezec=retezec, posun=posun)
elif input("Chceš šifrovat nebo odšifrovat? S/O") == "O":
    retezec = input("Zadej, co chceš zašifrovat")
    posun = int(input("Zadej o kolik chceš posunout"))
    odsifra(retezec=retezec, posun=posun)
 '''
 
#Napište funkci, která přijme seznam vět. O každé větě zjistí následující 3 informace, které z funkce vrátí v seznamu trojic:

#Délka věty
#Počet samohlásek
#Počet souhlásek
#Tedy co věta, to jedna trojice ve výsledném seznamu.

"""
from typing import List, Tuple

####################xxDŮLEŽITÉ

samohlasky = ["a", "e", "i", "o", "u"] 
souhlasky = ["h", "ch", "k", "r", "d", "t", "n"]
seznamvet = ['Mama sla nakoupit.', 'Ezoc buh.', 'Chyba je na nasi strane.']
vysledek = []

def zjistiUdaje(seznamvet: List) -> Tuple:
    for veta in seznamvet:
        pocet_slov = 0
        pocet_samohlasek = 0
        pocet_souhlasek = 0
        pocet_slov = (veta.count(' ')+1)
        
        for char in veta.lower():
            if char in samohlasky:
                pocet_samohlasek += 1
            elif char in souhlasky:
                pocet_souhlasek +=1
        vysledek.append((pocet_slov,pocet_samohlasek, pocet_souhlasek))
        
    return vysledek    
    
print(zjistiUdaje(seznamvet=seznamvet))

"""
''' 
##########ZEPTAT SE
pocet_prvku = int(input("Zadej počet prvků, pole kolika chceš vypočítat Pi"))

def aproximujPi(pocet_prvku: int)->float:
    prvky = [1, -(1/3)]
    for idx in range(2, pocet_prvku):
        if idx % 2 == 0:
            prvky.append(+(prvky[idx-1]+(1/2)))
        elif idx % 2 == 1:
            prvky.append(-(prvky[idx-1]+(1/2)))
    print(prvky)
    return sum(prvky)

print(aproximujPi(pocet_prvku=pocet_prvku))

 '''
'''  
from typing import List
 
samohlasky = ["a","e","i","o","u"]
souhlasky = ["h","ch","k","r","d","t","n"]
 
def ziskejSeznamVet()->List:
    seznam_vet = input("Zadej věty,oddělené pomlckou").split('-')
    return seznam_vet

def ziskejInformace(seznam_vet: List)->List:
    vysledek = []
    for veta in seznam_vet:
        pocet_slov = 0
        pocet_samohlasek = 0
        pocet_souhlasek = 0
        
        pocet_slov = veta.count(' ')+1
        
        for pismeno in veta.lower():
            if pismeno in samohlasky:
                pocet_samohlasek += 1
            elif pismeno in souhlasky:
                pocet_souhlasek += 1
                
        vysledek.append((pocet_slov, pocet_samohlasek, pocet_souhlasek))
    return print(vysledek)

def main():
    ziskejInformace(seznam_vet=ziskejSeznamVet())


if __name__ == "__main__":
    main()
    
 '''

''' OS13.3: Práce se souborem

Napište funkci, do které vložíte cestu k souboru. Funkce vrátí slovník, kde klíčem je slovo a hodnotou je jeho počet výskytů v textu souboru. Tento slovník bude následně funkcí vrácen. '''

from typing import Dict

cesta = "./test.txt"

def slovnik_ze_souboru(cesta: str)->Dict:
    slovnik = {}
 
    with open(cesta, "r") as soubor:
        vety = soubor.readlines()
        slova = ("".join(vety)).replace('.', '').lower().split()
        for slovo in slova:  
            if slovo in slova:
                slovnik[slovo] = slova.count(slovo)
    return print(slovnik)
    
    
slovnik_ze_souboru(cesta=cesta)
