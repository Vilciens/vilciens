import csv

with open('dati.csv', 'r') as fails:
    lasītājs = csv.reader(fails)
    for rinda in lasītājs:
        print(rinda)

with open('dati.csv', 'r') as fails: 
    lasītājs = csv.reader(fails)
    for rinda in lasītājs:
        print(rinda[0]) #nav braketes

import csv
arhivs = open("darbinieki.csv", "r", encoding = 'utf') # Atver csv failu
lasitajs = csv.reader(arhivs, delimiter=",") # Izveido CSV lasītāja objektu
for ieraksts in lasitajs: # Ciklā nolasa visus ierakstus
    vards = ieraksts[0] # Atlasa tikai vārda un nodarbošanās laukus
    nodarbosanas = ieraksts[3]
    print(f"{vards} - {nodarbosanas}") # Izdrukā ierakstu

arhivs.close() # Aizver csv failu