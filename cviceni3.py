#zadal_jmeno =  False

#while not zadal_jmeno:
#    jmeno = input("Zadej své jméno:")
#    if not jmeno:
#        print("Měl jsi zadat jméno ty ňoumo!")
#    else:
#        zadal_jmeno = True

#while True:
#    jmeno = input("Zadej své jméno:")
#    if not jmeno:
#        print("Měl jsi zadat jméno")
#    else:
#        break
    
#start = 50
#konec = 100
#inkrement = 5

#cislo = start
#while cislo <= konec:
#    print(cislo)
#    cislo += inkrement
    
#print("Haf mnau")


#start = 50
#konec = 100
#inkrement = 5

#for cislo in range(start, konec+1, inkrement):
#    print(cislo)


#zadane_udaje = False
#kod = 1234
#pokus = 0

#while not zadane_udaje:
#    if pokus < 3:
#        pokus += 1
#        sim_karta = int(input("Zadejte PIN SIM Karty:"))
#        if sim_karta == kod:
#            print("Úspěšně jste se přihlásili")
#            break
#        else:
#            print(f"Zadali jste špatný kód! Zbývající pokusy:{pokus}/3")
#    else:
#        print("SIM Karta byla zablokována!")
#        break
    
#import random

#vitezne_kombinace = [("kámen", "nůžky"), ("nůžky", "papír"), ("papír", "kámen")]

#pocet_vyhernich_kol = 2
#pocet_vitezstvi_hrac1 = 0
#pocet_vitezstvi_ai = 0

#while pocet_vitezstvi_hrac1 < pocet_vyhernich_kol and pocet_vitezstvi_ai < pocet_vyhernich_kol:
#    hrac1 = input("kámen, nůžky, papír")
#    ai = random.choice(["kámen", "nůžky", "papír"])
#    if (hrac1, ai) in vitezne_kombinace:
#        print("Hráč vyhrál kolo")
#        pocet_vitezstvi_hrac1 += 1
#    elif hrac1==ai:
#        print("Remíza")
#    else:
#        print("AI Vyhrálo kolo")
#        pocet_vitezstvi_ai += 1

#if pocet_vitezstvi_hrac1 == 2:
#    print("Hráč získal 2 vítezná kola")
#elif pocet_vitezstvi_ai == 2:
#    print("AI získalo 2 vítězná kola.")


#from PIL import Image

#obrazek = Image.open('C:/Users/Uživatel/OneDrive/Plocha/habik.jpg')

#sirka,vyska = obrazek.size

#for x in range(sirka):
#    for y in range(vyska):
#        if y < 50:
#            for x in range(sirka):
#                obrazek.putpixel((x,y), (0+20,0+20,0+20))
                
#        r,g,b = obrazek.getpixel((x,y))    
    
#obrazek.show()


#hodnota = False

#while not hodnota:
#    hodnota = input("Zadejte hodnotu").isdigit()
#    if not hodnota:
#        print("číslo není Integer")    
#    else:
#        print("Číslo je Integer")        


"""

import statistics

# Průměr z kolekce čísel

stats = statistics
kolekce = []


stop = False


while not stop:
    vstup = input("Zadejte číslo:")
    if vstup == "STOP":
        stop = True
    else:
        stop = False
        kolekce.append(int(vstup))
        prumer = sum(kolekce) / len(kolekce)
        median = stats.median(kolekce)
        stredniHodnota = stats.mean(kolekce)
        print(median, stredniHodnota, prumer)
        
"""



import random


otazky = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

otazky_pocet = len(otazky)

while not otazky_pocet == 0:
    stisk = input("Stiskněte ENTER pro vylosování otázky")
    if otazky_pocet >= 1:
        losovana_otazka = otazky[random.randint(0,len(otazky)-1)]
        print(losovana_otazka)
        otazky.remove(losovana_otazka)
        otazky_pocet = len(otazky)
    else:
        print(otazky)
        print("Otázky došly")
        
        
""" 
while otazky:
    input()
    otazka = random.choice(otazky)
    otazky.remove(otazka)
    print(otazka)
"""

''' import tkinter as tk

window = tk.Tk()

window.title("Šejbyho okno")

window.geometry("800x600")

novyLabel = tk.Label(text = "Okynko")




novyLabel.grid(column=0, row=0)

window.mainloop() '''


 
''' sudaCisla = []
lichaCisla = []

for x in range(0,101):
    if x % 2 == 0:
        sudaCisla.append(x)
    else:
        lichaCisla.append(x)

sudaCisla.sort(reverse=True)
lichaCisla.sort(reverse=False)

pocet = sudaCisla.count(2)

print(sudaCisla)
 '''


''' a = int(input("Zadej A:"))
op = input("Zadej operátor")
b = int(input("Zadej B:"))


def scitani(a,b):        
    c = a + b
    print(c)
    
def odcitani(a,b):
    c = a - b
    print(c)
    
def nasobeni(a,b):
    c = a * b
    print(c)
    
def deleni(a,b):
    c = a / b
    print(c)


match op:
    case "+":
        scitani(a,b)
    case "-":
        odcitani(a,b)
    case "*":
        nasobeni(a,b)
    case "/":
        deleni(a,b)
        

 '''



uzivatele = [(Honza, 1234)]




















   


        
    
    


    