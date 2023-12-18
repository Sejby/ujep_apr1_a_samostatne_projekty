import os
import shutil

# os.system("echo haf haf > soubor.txt") 
# os.system("dir")


# Vytvořte kod, ktery vytvori 5 adresaru s nazvy ADR1,ADR2 az ADR5
# V každém adresáři bude 10 soubor S1.txt, S2.txt az S10.txt
# V kazdem souboru bude napsáno AHOJ


"""

for i in range(1,6):
    os.system(f"mkdir ADR{i}")
    for j in range(1,11):
        os.system(f"cd ADR{i} && echo AHOJ > S{j}.txt")


"""

# prepsat vas kod aby byl platformově agnosticky

# os.mkdir()
# os.listdit()
# os.chdir()
# with open

"""

for i in range(1,6):
    os.mkdir(f"ADR{i}")
    for j in range(1,11):
        os.chdir("ADR{i}")
        with open(f"S{j}.txt", "w") as f:
            f.write("AHOJ")
            os.chdir("..")
            
"""
"""
os.mkdir("ADR1")
os.chmod("ADR1", 0o777)

with open("ADR1", "w") as f:
    f.write("haf haf")

os.rmdir("ADR1")
"""

# Napište funkci, do které vložíté cestu k adresáři a funkce smaže vše uvnitř adresáře, včetně soubor v podadresářích tak, aby šlo pomoci rmdir zadany adresar smazat
# provedte pomoci rekurze
''' 
shutil.copy
shutil.copy2
shutil.copytree
shutil.rmtree
shutil.move
shutil.disk_usage '''

# napište funkci, která přijme jako parametr cestu k adresáři
# funkce prohledá všechny adresáře v zadaném adresáři a všechny soubory v adresářích, které
# začínají na samohlásky zkopíruje do adresáře samohlásky. Všechny ostatní do adresáře souhlasky

# vstup - zdroj/ADR1/ahaf.txt, zdroj/ADR1/blek.txt, zdroj/ADR2/ehlem.txt
# vystup - samohlasky/ahaf.txt, samohlasky/ehlem.txt, souhlasky/blek.txt

cesta = "zdroj"

samohlasky = ["a","e","i","o","u", "y"]


def vratSouborySamohlasky(cesta: str):
    pracovni_adresar = os.getcwd()
    os.chdir(cesta)
    podadresare = os.listdir()
    print(podadresare)
    for podadresar in podadresare:
        os.chdir(podadresar)
        soubory = os.listdir()
        print(soubory)
        for soubor in soubory:
            if soubor[0] in samohlasky:
                shutil.copy2(soubor, pracovni_adresar + "/" + "samohlasky/" + soubor)
            else:
                shutil.copy2(soubor, pracovni_adresar + "/" + "souhlasky/" + soubor)
        os.chdir("..")

#naleznete všechny soubory v adresari a zkopirujte jejich textovy obsah do jednoho spolecneho textoveho souboru

# soubor1.txt -> ahoj
# soubor2.txt -> cau
# blabla.txt -> mnau mnau

# spolecne.txt -> ahoj mnaumnau

# napište funkci pomoci lambda a filter do ktere vlozite seznam retezcu a ona vyfiltruje ty, ktere maji pocet samohlasek < 3

#napiste funkci do ktere vlozite seznam slov a ona vam vrati kolikrat se tam nachazi velkych a malych pismen. Vratte to jako slovnik, kde klicem je male a velke a hodnotu je jejich pocet

from typing import Dict
from collections import Counter

retezec = "Haha ty jsi ale budulínek"


def zjistiMalaVelkaPismena(retezec: str)->Dict:
    vysledek = {}
    for pismeno in "".join(retezec.split()):
        vysledek[pismeno] = retezec.count(pismeno)
    
    return vysledek


print(zjistiMalaVelkaPismena(retezec=retezec))