"""
from typing import List

seznam = [("Honza", "123")]

def registrujUzivatele(seznam: List) -> None:
    jmeno = input("Zadej jméno")
    heslo = input("Zadej heslo")
    if not (jmeno,heslo) in seznam:
        seznam.append((jmeno, heslo))
        print("Jste zaregistrován")
    else:
        print("Již jste registovaný")
        registrujUzivatele(seznam=seznam)
            
        
registrujUzivatele(seznam=seznam)

""""