
vek = int(input("Kolik ti je let?"))





if vek >= 18:
    print("Na tady máš pivo, chlastej!")

elif vek < 15:
    print ("Na tady máš Jupíka, bumbej")

else:
  print("Na tady máš zubní pastu = Zelená")




print("Zavíračka")




disponibilni_hodiny = 2
znamka = int(input("Stahnuti znamky: "))

if znamka == 1:
  disponibilni_hodiny += 1
elif 2 <= znamka <= 3:
  pass
elif znamka in [4,5]:
  disponibilni_hodiny -= 1
else:
  print("Chyba neklasifikováno!")

print(f"Máš k dispozici {disponibilni_hodiny} hodin k hraní Fortnite.")




#BMI
vyska = float(input("Zadejte výšku v m:"))
hmotnost = int(input("Zadejte hmotnost v kg:"))

vysledek = round(hmotnost / vyska**2, 1)

if vysledek <= 17:
  print(f"Vaše BMI je: {vysledek}, máte silnou podváhu!")
elif vysledek > 17 and vysledek <= 18.5:
  print(f"Vaše BMI je: {vysledek}, máte slabou podváhu!")
elif vysledek > 18.5 and vysledek <= 25:
  print(f"Vaše BMI je: {vysledek}, máte optimální váhu!")
elif vysledek > 25 and vysledek <= 30:
  print(f"Vaše BMI je: {vysledek}, máte slabou nadváhu!")
elif vysledek > 30 and vysledek <= 35:
  print(f"Vaše BMI je: {vysledek}, máte obezitu!")
elif vysledek > 35 and vysledek <= 40:
  print(f"Vaše BMI je: {vysledek}, máte střední obezitu!")
elif vysledek > 40:
  print(f"Vaše BMI je: {vysledek}, máte silnou obezitu!")


#Výpočet kvadratické rovnice:
import math


a = float(input("Zadejte hodnotu a na druhou v rovnici:"))
b = float(input("Zadejte hodnotu b v rovnici:"))
c = float(input("Zadejte hodnotu c v rovnici:"))

Diskriminant = (b**2) - (4*a*c)



if Diskriminant == 0:
  vypocetx1 = (-b + math.sqrt(Diskriminant)) / (2*a)
  print(f"Výsledek je: x1 = {vypocetx1}")

elif Diskriminant < 0:
  print("Nemá řešení.")

elif Diskriminant > 0:
  vypocetx1 = (-b + math.sqrt(Diskriminant)) / (2*a)
  vypocetx2 = (-b - math.sqrt(Diskriminant)) / (2*a)
  print(f"Výsledek je: x1 = {vypocetx1}, x2 = {vypocetx2}")



#Kámen, nůžky, papír
import random

hrac1 = input("kámen, nůžky, papír")
ai = random.choice(["kámen", "nůžky", "papír"])


vitezne_kombinace = [("kámen", "nůžky"), ("nůžky", "papír"), ("papír", "kámen")]


if (hrac1, ai) in vitezne_kombinace:
  print("Hráč vyhrál")
elif hrac1==ai:
  print("Remíza")
else:
  print("AI Vyhrálo")


#heslo
import string

#heslo

heslo = input("Zadej své heslo:")
mala_pismena = False

for pismeno in heslo:
  if pismeno in string.ascii_lowercase:
      mala_pismena = True




