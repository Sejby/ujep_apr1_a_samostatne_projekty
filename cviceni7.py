# Metoda Monte Carlo
#import random
#import math

"""
def ziskej_cislo_z_klavesnice(hlaska):
    cislo = input(hlaska)
    je_cislem = cislo.replace('.','').isdigit()
    return cislo, je_cislem

def ziskej_polomer_kruznice():
    hlaska = "Zadej poloměr kružnice"
    cislo, je_cislo = ziskej_cislo_z_klavesnice(hlaska)
    while not je_cislo:
        ziskej_cislo_z_klavesnice(hlaska)
    return float(cislo)

def nahodne_vystrel(xmeze, ymeze):
    nahodne_x = random.uniform(xmeze[0], ymeze[1])
    nahodne_y = random.uniform(xmeze[0], ymeze[1])
    return nahodne_x, nahodne_y

def zjisti_zda_trefa(randx, randy, stred_kruznice, polomer):
    dx = stred_kruznice - randx
    dy = stred_kruznice - randy
    vzdalenost = math.sqrt(dx**2 + dy**2)
    return vzdalenost <= polomer

def spocitej_obsah_monte_carlo(npokusu, polomer_kruznice):
    # Skruznice = Sctverce * nhit/nshots
    ntref = 0
    obsah_ctverce = (polomer_kruznice*2)**2
    for istrela in range(npokusu):
        #náhodný výstřel do kružnice
        nahodne_x, nahodne_y = nahodne_vystrel((0, polomer_kruznice*2),(0, polomer_kruznice*2))
        if zjisti_zda_trefa(nahodne_x, nahodne_y, polomer_kruznice, polomer_kruznice):
            ntref += 1
    return obsah_ctverce * ntref/npokusu
            
def vytiskni_vysledky(polomer, obsah):
    print(f"Kružnice o poloměru {polomer} má obsah {obsah}")

def main():
    polomer = ziskej_polomer_kruznice()
    obsah = spocitej_obsah_monte_carlo(npokusu=10000, polomer_kruznice=polomer)
    vytiskni_vysledky(polomer, obsah)
        
if __name__ == "__main__":
    main()
"""

    

#Napište program, která získá od uživatele login a heslo. Pokud uživatel je v seznamu registrovaných uživateků, tak ho přivítá. V opčaném případě se
# ho zeptá zda se chce registrovat. Pokud ano, přidá ho do seznamu

# Napište program, která získá od uživatele jaké těleso a jaké veličiny chce spočítat (objem, obsah). Následně tyto veličiny (hodnoty) vypíše na obrazovku.

"""
seznam = [("honza", "123"), ("Karel", "xd")]

def ziskej_login():
    jmeno = input("Zadej uživatelské jméno:")
    heslo = input("Zadej heslo:")
    return jmeno,heslo

def je_zaregistrovan()->bool:
    jmeno,heslo = ziskej_login()
    if (jmeno,heslo) in seznam:
        print("Vítej!")
        return True
    else:
        hlaska = input("Chceš se zaregistrovat? A/N")
        if hlaska == "A":
            zaregistruj()
        else:
            return False

def zaregistruj():
    jmeno, heslo = ziskej_login()
    seznam.append((jmeno,heslo))
    print("Byl jsi úspěšně zaregistrován")
    print(seznam)


def main():
    je_zaregistrovan()

if __name__ == "__main__":
    main()

"""
"""
import math

telesa = ['krychle', 'koule']
veliciny = ['obsah', 'objem']


def ziskej_input():
    str_teles = input(f"Zadej tělesa, která chceš spočítat: {telesa} Tělesa odděl čárkou")
    str_velicin = input(f"Zadej veličiny, které chceš spočítat: {veliciny}, veličiny odděl čárkou")
    return str_teles,str_velicin

def preved_input_na_pole():
    str_teles,str_velicin = ziskej_input()
    pole_teles = str_teles.split(',')
    pole_velicin = str_velicin.split(',')
    print(pole_teles, pole_velicin)
    return pole_teles, pole_velicin

def vypis():
    pole_teles, pole_velicin = preved_input_na_pole()
    for tvar in pole_teles:
        match tvar:
            case "krychle":
                a = int(input("Zadej parametr a:"))
                if "objem" in pole_velicin and "obsah" in pole_velicin:
                    vypocitej_objem_krychle(a)
                    vypocitej_obsah_krychle(a)
                elif "objem" in pole_velicin:
                    vypocitej_objem_krychle(a)
                elif "obsah" in pole_velicin:
                    vypocitej_obsah_krychle(a)
            case "koule":
                polomer = int(input("Zadej poloměr:"))
                if "objem" in pole_velicin and "obsah" in pole_velicin:
                    vypocitej_objem_koule(polomer)
                    vypocitej_obsah_koule(polomer)
                elif "objem" in pole_velicin:
                    vypocitej_objem_koule(polomer)
                elif "obsah" in pole_velicin:
                    vypocitej_obsah_koule(polomer)

def vypocitej_objem_krychle(a):
    objem = a**3
    print(f"Objem krychle je {objem}")
    return objem
            
def vypocitej_obsah_krychle(a):
    obsah = 6*(a**2)
    print(f"Obsah krychle je {obsah}")
    return obsah

def vypocitej_objem_koule(polomer):
    objem = (4/3)*math.pi*(polomer**3)
    print(f"Objem koule je {objem}")
    return objem

def vypocitej_obsah_koule(polomer):
    obsah = 4*math.pi*(polomer**2)
    print(f"Obsah koule je {obsah}")
    return obsah

def main():
    vypis()
    
if __name__ == "__main__":
    main()
    
"""
"""
import math
hodnoty = {
   "a": 0,
   "b": 0,
   "c": 0,
   "r": 0
}
vysledek = 0

def objekt():
    teleso = input("Napište jaké těleso by jste chtěli vypočítat: ")
    return teleso

def kvadr(hodnoty, vysledek):
    hodnoty["a"] = float(input("Zadej délku strany a: "))
    hodnoty["b"] = float(input("Zadej délku strany b: "))
    hodnoty["c"] = float(input("Zadej délku strany c: "))
    otazka = input("Chcete spočítat objem nebo obsah: ")
    if otazka.lower() == "objem":
        vysledek = (hodnoty["a"]*hodnoty*["b"]*hodnoty["c"])
    if otazka.lower() == "povrch":
        vysledek = 2*((hodnoty["a"]*hodnoty["b"])+(hodnoty["a"]*hodnoty["c"])+(hodnoty["b"]*hodnoty["c"]))
    return vysledek

def krychle(hodnoty):
    hodnoty["a"] = int(input("Zadej délku strany a: "))
    otazka = input("Chcete spočítat objem nebo obsah: ")
    if otazka.lower() == "objem":
        vysledek = hodnoty["a"]**3
    if otazka.lower() == "povrch":
        vysledek = 6*(hodnoty["a"]**2)
    return vysledek

def koule(hodnoty):
    hodnoty["r"] = int(input("Zadej délku poloměru r: "))
    otazka = input("Chcete spočítat objem nebo obsah: ")
    if otazka.lower() == "objem":
        vysledek = (4/3)*math.pi*(hodnoty["r"]**3)
    if otazka.lower() == "povrch":
        vysledek = 4*math.pi*(hodnoty["r"]**2)
    return vysledek 


def zobrazeni_vysledku(teleso, vysledek):
   print(f"Vase vybrané těleso {teleso} má {vysledek}")

def main(teleso):
    if teleso == "kvádr":
     zobrazeni_vysledku(teleso, kvadr(hodnoty))
    elif teleso == "krychle":
     zobrazeni_vysledku(teleso, krychle(hodnoty))
    elif teleso == "koule":
     zobrazeni_vysledku(teleso, koule(hodnoty))

main(objekt())

"""

"""
import random

print("Hraješ hru uhádni číslo, postupuj podle pokynů:")

def zjisti_input(hadanka):
    while True:
        cislo_str = input("Zadej číslo: ")
        if cislo_str.isdigit():
            cislo = int(cislo_str)
            porovnani(cislo, hadanka)
            break
        else:
            print("Neplatný vstup. Zadej prosím celé číslo.")

def porovnani(cislo, hadanka):
    if cislo == hadanka:
        uhodnuto(cislo)
    elif cislo < hadanka:
        print(f"Hádané číslo je větší než {cislo}")
        zjisti_input(hadanka)
    else:
        print(f"Hádané číslo je menší než {cislo}")
        zjisti_input(hadanka)

def uhodnuto(cislo):
    print(f"Uhodnul jsi! Číslo bylo {cislo}")

def zjisti_min_max():
    while True:
        min_str = input("Zadej minimální rozsah: ")
        max_str = input("Zadej maximální rozsah: ")
        if min_str.isdigit() and max_str.isdigit():
            min_val = int(min_str)
            max_val = int(max_str)
            if min_val < max_val:
                return min_val, max_val
            else:
                print("Neplatný rozsah. Minimální hodnota musí být menší než maximální hodnota.")
        else:
            print("Neplatný vstup. Zadej prosím celá čísla.")

def hadane_cislo(min, max):
    return random.randint(min, max)

def hra():
    min_val, max_val = zjisti_min_max()
    hadanka = hadane_cislo(min_val, max_val)
    zjisti_input(hadanka)

def main():
    hra()

if __name__ == "__main__":
    main()
"""