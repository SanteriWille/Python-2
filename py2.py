# Oppgave 1
number = int(input("Skriv inn et tall: "))
i = number

while i > 0:
  print(i)
  i -= 1

# Oppgave 2
brkTall = int(input("Skriv inn et tall: "))
for x in range (1, 11):
  print(brkTall, "X" , x, " = ", (brkTall*x))

# Oppgave 3
import random
rnumber = random.randint(1, 100)
print(rnumber)
usrnumber = int(input("Skriv inn et tall mellom 1 og 100: "))

while usrnumber != rnumber:
  if usrnumber < rnumber:
    print("Tallet er for lavt")
    usrnumber = int(input("Skriv inn et tall: "))
  elif usrnumber > rnumber:
    print("Tallet er for høyt")
    usrnumber = int(input("Skriv inn et tall: "))
  
print("Gratulerer du gjettet riktig! Tallet er:", rnumber)

# Oppgave 4
for prmNumber in range(1, 100):  
    if prmNumber > 1:
        for x in range(2, (prmNumber // 2) + 1):
            if (prmNumber % x) == 0:
                print(prmNumber, "er ikke et primtall")
                break
        else:
            print(prmNumber, "er et primtall")
    else:
        print(prmNumber, "er ikke et primtall")

# Oppgave 5
from math import pi

sNumber = int(input("Skriv inn radiusen til for en sirkel: "))
area = pi * sNumber ** 2
print("Arealet av en sirkel med radius " + str(sNumber) + " er: " + str(area))  

# Oppgave 6
antallOrd = 0

while True:
    tekst = input("Skriv en setning (eller 'stopp' for å avslutte): ").strip()

    if tekst.lower() == "stopp":
        break

    ordListe = tekst.split()
    antallOrd += len(ordListe)  

print("Totalt antall ord skrevet:", antallOrd)