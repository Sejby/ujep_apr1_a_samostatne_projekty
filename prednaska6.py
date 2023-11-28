nl = [1,2,3,4,5]
sl = ["Faramir", "Bormoir"]

"""
[sl] => map f => [f(s1)]

f = unární funkce (má jeden parametr) - mapovací funkce (mapping) = zobrazení
"""

"""
result = []
for item in sl:
    result.append(item[::-1])
print(result)

"""

# Komprehenze (seznamové)

# print([2*item for item in nl])

# print([item[::-1] for item in sl])

# Operace filtr
# Vytváří nový seznam, který obsahuje jen ty položky původního seznamu, které splňují nějakou podmínku.

# podmínka: unární funkce vracející True nebo False (bool) tj. "predikát"

# Odfiltrovat z číselného seznamu sudé položky

result = []
"""
for item in nl:
    if item % 2 == 1:
        result.append(item)
print(result)"""

#[[item] for item in nl if item % 2 == 1]

#[len(item) for item in sl if "o" in item]

# Lze používat i komprehenze, které zároveň mapují a filtrují
# Počet znaků u všech řetězců ze seznamu ˇslˇ, které obsahují písmeno "o"

# Reduce (redukce)
# seznam hodnot, na níž aplikujeme tzv. agregační funkci, která vždy spojí opakovanou aplikací získáme jedinou výslednou hodnotu

''' 
suma = 0
for item in nl:
    suma = suma + item #kroko redukce
print(suma)

 '''

# Dva typy redukce:
    # s počáteční hodnotou: funguje i s prázdným seznamem, ale je nutné zvolit správnou počáteční hodnotu
    # bez počáteční hodnoty : měla by fungovat až dvou prvků (u jednoprvkových je výsledek jediná položka)

"""    
sum([1,2,3,6])
    
max(["želva", "rorýs", "chameleon"])
    
from functools import reduce

reduce(add, sl)
"""

i, j = 2, 3 # složené přiřazení (i, j) = (2, 3)
i, j = j, i #pythonský idiom pro swap (prohození)
[i, j] = [j, i] # lze přiřazovat i seznamy (málo přehledné, méně efektivní)
[i, j] = (i, j)
(i, j) = [i, j]
list((1,2))
tuple([1,2])








"""
from typing import List

arr = [10,1,3,6,7,8,9,2,4,5]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
             if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    print(arr)
    
bubbleSort(arr=arr)
 
"""
import Timer

biglist = [1,4,6,2309,1298,7248]

%timeit sum(len(number) for number in biglist)