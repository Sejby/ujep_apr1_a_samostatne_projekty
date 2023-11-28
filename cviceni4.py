''' 
seznam = ["K", "M", "N"]
usporadana_ntice = ()
mnozina = {"1", "2", "3"}


kamaradi = ["Pepa", "jana", "Pepa", "Tomas", "ALena", "Pepa"]
kamaradi = list(set(kamaradi)) #odstraní duplicity
print(kamaradi)

prihlaseni = [("Pavel", "123"), ("Jiri", "Skvor")]

kamaradi = ["Pepa", "jana", "Pepa", "Tomas", "ALena", "Pepa"]


pocet_kamaradu = len(kamaradi)

kamaradi(kamaradi[pocet_kamaradu-1]) '''



"""
samohlasky = ["a", "e", "i", "o", "u", "y"]

jmena = ["Pavel", "Milan", "Alena", "Rostislavomir"]
vysledek = []


for jmeno in jmena:
    pocet_samohlasek = 0
    for samohlaska in samohlasky:
        pocet_samohlasek += jmeno.lower().count(samohlaska)
    vysledek.append((jmeno, pocet_samohlasek))
    
print(vysledek)

"""



#Šibenice
"""
tajenka = "boruvka"

odkryta_pole = ["_"] * len(tajenka)
pocet_zivotu = 7

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


idx_sibenice = 0

while "_" in odkryta_pole and pocet_zivotu > 0:
    print(f"Počet životů: {pocet_zivotu}\n"," ".join(odkryta_pole))
    pismenko = input("Zadej písmeno:")
    if pismenko not in tajenka:
        print(HANGMANPICS[idx_sibenice])
        print(f"Pismenko {pismenko} se v tajence nenachází")
        pocet_zivotu -= 1
        idx_sibenice += 1
    else:
        for idx_odkryti, pismeno_tajenky in enumerate(tajenka):
            if pismeno_tajenky == pismenko:
                odkryta_pole[idx_odkryti] = pismenko

if "_" not in odkryta_pole and pocet_zivotu > 0:
    print(f"Výsledek: {tajenka} \nUhádl jsi vše!")
    
elif "_" in odkryta_pole and pocet_zivotu <= 0:
    print("Jsi oběšen!")

"""

"""
#Přihlašovací systém
registrovani = [('Pavel', '1234'), ('Zbysek', 'heslo')]

print("Chcete se přihlásit nebo zaregistrovat?")
logorreg = input("Stiskněte L nebo R")

if logorreg == "L":
   
    jmeno = input("Zadejte username:")
    heslo = input("Zadejte heslo:")

    for idx in range(len(registrovani)):
        if jmeno in registrovani[idx] and heslo in registrovani[idx]:
            print("Úspěšně přihlášen!")
        elif jmeno in registrovani[idx] and heslo not in registrovani[idx]:
            print("Špatné heslo!")
        elif jmeno not in registrovani:
            print("Musíte se zaregistrovat!")
            break
elif logorreg == "R":
    reg_jmeno = input("Zadejte uživatelské jméno:")
    reg_heslo = input("Zadejte heslo")
    
    registrovani.append((reg_jmeno, reg_heslo))
    print(registrovani)
    
"""
