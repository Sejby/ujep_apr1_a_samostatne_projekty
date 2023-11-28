#Funkcionální programování

#from random import randint

#nahodna_cisla = [randint(0,9) for cislo in range(10)]

import matplotlib.pyplot as plt
from random import randint, choice
from string import ascii_lowercase


''' 
obrazek = []
for i in range(50):
    radek = []
    for j in range(50):
        radek.append((0,255))
    obrazek.append(radek)
 '''

''' obrazek = [[randint(0,255) for j in range(100)] for i in range(50)]
plt.imshow(obrazek, cmap="gray")

 '''
 
''' licha_cisla = [cislo for cislo in range(50,100) if cislo % 2 == 1]
print(licha_cisla)




nahodne_slovo = ["".join([choice(ascii_lowercase) for p in range(8)]) for islovo in range(10)]
print(nahodne_slovo)
  '''
  
  
# delka_jmena = list(map(len, input("Zadej kolekci jmen, oddělené čárkou").split(",")))
''' 
def obrat_jmeno(jmeno):
    return jmeno[::-1]
    

jmena = ['Honza', 'Ezoc']
vysledek = []

jmena_pozpatku = list(map(obrat_jmeno, jmena))
print(jmena_pozpatku) '''



# LAMBDA funkce - anonymní funkce, nejdou volat, ale lze je aritmeticky využít

# lambda cislo: 2*cislo+3

''' slovni_hodnoceni = ['vyborne', 'chvalitebne', 'dobre', 'dostatecne', 'nedostatecne']

znamky = list(map(int, input("Zadejte známky oddělené mezerou: ").split()))
znamky = list(filter(lambda znamka: 1<=znamka<=5, znamky))
znamky = list(map(lambda znamka: slovni_hodnoceni[znamka-1], znamky))

print(znamky) 
 '''

"""
upravy = {
    "zesvetli": lambda px: px+10,
    "ztmav": lambda px: px-10,
}

px = 50
volba = input(f"Vyber si {list(upravy.keys())}")
print(upravy[volba](px))

"""