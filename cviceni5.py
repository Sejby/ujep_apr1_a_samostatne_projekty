
"""
from string import ascii_lowercase


veta = "Pes po kole jel. Pes jel na kole. Kolo jelo po psovi."

citac_slov = {}

for pismeno in ascii_lowercase:
    citac_slov[pismeno] = 0

for slovo in veta:
    upravene_slovo = slovo.replace(".", "").lower()
    if upravene_slovo in citac_slov:
        citac_slov[upravene_slovo] += 1
    else:
        citac_slov[upravene_slovo] = 1
        



print(citac_slov)

"""

veta_cz = "Pes stekal na postaka a pak ho zabil"
veta_en = ""

slovnik = [{
    "jazyk": "en",
    "pes": "dog",
    "stekal": "woof woof",
    "postaka": "postman",
    "zabil": "vaporized",
    "na":"on",
    "a":"and",
    "pak":"then",
    "ho":"him"
},
{
    "jazyk": "de",
    "pes": "Hund",
    "stekal": "er bellte",
    "postaka": "Briefträger",
    "zabil": "getötet",
    "na": "an",
    "a": "und",
    "pak": "dann",
    "ho": "ihn"           
               
}]


for idx in range(len(slovnik)):
    slova_cz = veta_cz.lower().split()
    veta_en = " ".join([slovnik[idx].get(slovo, slovo) for slovo in slova_cz])    
    print(veta_en) 



"""

teplice = {
    "pocet_obyvatel": 50000,
    "rozloha": "10km2",
    "krajske_mesto": False,
    "starosta": "Hynek Hanza",
    "kvalita vody": "dobrá",
    "nezaměstnanost": 1.4,
    
    "pamatky":{
        "morovy_sloup": "sloup na náměstí svobody",
        "muzem": "muzeum na náměstí svobody",
        "sanov": "Šanov I, původní část Teplic",
        "botanicka_zahrada": "rozlehlá botanická zahrada v okolí Šanova II",
          
    },
    
    "zakladni_skoly": {
        "zs_kopernikova":{
            "stupen_vzdelani": "zakladni",
            "zamereni": "obecne",
            "adresa": "Kopernikova, Šanov II, Teplice",
            "kontakt": "+420 978 238 854"
        },
        
        "zs_buzulucka":{
            "stupen_vzdelani": "zakladni",
            "zamereni": "rozsirena vyuka matematiky a informatiky",
            "adresa": "Buzulucká, Řetenice, Teplice",
            "kontakt": "+420 378 238 223"
        },
    },
    
    "stredni_skoly":{
        "sps_teplice":{
            "stupen_vzdelani": "stredni",
            "zamereni": "průmyslová škola",
            "adresa": "Benešovo nám., Teplice",
            "kontakt": "+420 123 238 854"
        },
        
        "gymnazium_teplice":{
            "stupen_vzdelani": "zakladni a stredni",
            "zamereni": "obecne",
            "adresa": "Alejní, Teplice",
            "kontakt": "+420 078 238 223"
        },
    },   
}

def dotaz_na_hodnotu(slovnik, cesta=[]):
    print(f"Aktuální cesta: {', '.join(cesta)}")

    klíče = list(slovnik.keys())
    print("Dostupné klíče:", klíče)

    dotaz = input("Který klíč vás zajímá? Zadejte klíč nebo 'q' pro ukončení: ")

    if dotaz == 'q':
        return

    if dotaz in klíče:
        cesta.append(dotaz)
        nový_slovnik = slovnik[dotaz]

        if isinstance(nový_slovnik, dict):
            dotaz_na_hodnotu(nový_slovnik, cesta)
        else:
            print(f"{dotaz}: {nový_slovnik}")
    else:
        print("Neplatný klíč. Zadejte platný klíč.")

dotaz_na_hodnotu(teplice)

"""

"""

trida = {
    'Jan': [4,5,3,1,2,5,4,3,2,1],
    'Eva': [5,5,5,3,3,2,1,4,5],
    'Petr': [3,4,4,2,1,1,1,1,4,3],
}


celkova_suma = 0
pocet_znamek = 0

for student, znamky in trida.items():
    celkova_suma += sum(znamky)
    pocet_znamek += len(znamky)

if pocet_znamek == 0:
    prumer_tridy = 0
else:
    prumer_tridy = celkova_suma / pocet_znamek

print(f'Průměrná známka třídy: {prumer_tridy}')

"""

"""
import random

# Generátor náhodného počtu klíčů (1 až 10)
pocet_klicu = random.randint(1, 10)

slovnik = {}

for i in range(pocet_klicu):
    klic = f'klíč{i}'
    hodnoty = [random.randint(1, 100) for _ in range(10)]  # Seznam 10 náhodných čísel od 1 do 100
    slovnik[klic] = hodnoty

print(slovnik)
"""