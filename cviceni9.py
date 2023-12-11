##Práce se souborem
## Typová úloha do zápočtu
# Napište funkci vrat prumerne znamky, ktera prijme cestu k souboru se znamkami a vrati slovnik, 
# kde klicem bude jmeno studenta a hodnotou ke klici bude prumerna znamka


''' from typing import Dict

cesta = './znamky.txt'
    
def vratPrumer(cesta: str)->Dict:
    prumerne_znamky = {}
    with open(cesta, "r") as f:
        text = f.read()
        for radek in text.split("\n"):
            if radek:
                jmeno,znamky = radek.split(":")
                znamky = list(map(int, znamky.split(",")))
                prumerna_znamka = sum(znamky)/len(znamky)
                prumerna_znamka = round(prumerna_znamka, 2)
                prumerne_znamky[jmeno] = prumerna_znamka
    return prumerne_znamky 

print(vratPrumer(cesta=cesta))
 '''

"""
with open("./data.txt", "a") as soubor:
    soubor.write("baf baf")
"""

# napište program, který se opakovaně uživatele ptá na následující data z klávesnice: jméno klienta, finance na účtě
# jakmile napíše uživatel STOP na klávesnici, tak program přestane žádat o nová data
# následně program vytvoří soubor klient.csv a zapíše do prvního sloupce s nadpisem klient na jednotlivé řádky
# jména klientů a do sloupce finance napíše na jednotlivé řádky finance na účtě na účtě příslušných klientů
# zkontrolujte, že se jedná o reálnou tabulku (umí to colab, excel, google tabulky, etc.)

from typing import List

"""
def zapisUzivatele() -> List:
    klienti = []
    stop = False
    while not stop:
        vstup = input("Zadejte své jmeno a finance oddělené čárkou nebo STOP pro zastavení")
        if vstup == "STOP":
            stop = True
        else:
            jmeno,finance = vstup.split(",")
            finance = int(finance)
            klienti.append((jmeno,finance))
    return klienti
            
def zapisDoSouboru(klienti) -> None:
    with open("./klienti.csv", "w") as soubor:
        soubor.write("klient,finance\n")
        for jmeno,finance in klienti:
            soubor.write(f"{jmeno},{finance}\n")
        suma_financi = sum([finance for jmeno, finance in klienti])
        prumer_financi = suma_financi/len(klienti)
        soubor.write(f"{suma_financi},{prumer_financi}")


def main():
    zapisDoSouboru(klienti=zapisUzivatele())
    

if __name__ == "__main__":
    main()
    
"""

## Vyjímky
''' from math import inf


try:
    delenec = 5
    delitel = int(input("Zadej číslo"))
    podil = delenec/delitel
except ZeroDivisionError:
    print("Dělil jsi nulou")
    podil = inf
except ValueError:
    print("Zadal jsi něco co není číslo")
    podil = None
except:
    print('\nNeznámá chyba. Prosim kontaktujte admina postovnim holubem')
    podil = None
else:
    print("Všechno proběhlo v pohodě jsem rad ze umis zadat cislo")
finally:
    print(podil)
    print("konec programu") '''
    
def secti(a, b):
    soucet = a+b
    return soucet

assert secti(a=5,b=10)


#TDD (Vývoj řízený testy)

def secti(a,b):
    return 7
    
def test_secti_dve_cisla():
    #AAA framework (arrange,act,assert)
    vstup1, vstup2 = 2,5
    vystup = secti(a=vstup1, b=vstup2)
    assert vystup == 7

def secti(a,b):
    ...
    
def testrunner():
    test_secti_dve_cisla()
    
testrunner()
    