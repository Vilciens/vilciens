import csv

# Atver failu rakstīšanas režīmā
with open('skoleni.csv', 'w', newline='', encoding='utf-8') as fails: # Izveido CSV rakstītāju
    # Ieraksta kolonnu nosaukumus
    rakstitajs.writerow(['vards', 'uzvards', 'klase'])
 
    # Pieprasām lietotājam ievadīt datus
    vards = input("Ievadi 5 vārdus: ")
    uzvards = input("Ievadi 5 uzvārdus: ")
    klase = input("Ievadi 5 klases: ")
    # Ieraksta datus CSV failā
    rakstitajs.writerow([vards, uzvards, klase])