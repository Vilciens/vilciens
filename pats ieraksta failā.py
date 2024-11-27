import csv

# Atver failu rakstīšanas režīmā
with open('skoleni.csv', 'w', newline='', encoding='utf-8') as fails: # Izveido CSV rakstītāju
    # Ieraksta kolonnu nosaukumus
    rakstitajs.writerow(['vards', 'uzvards', 'klase'])
    for i in range(5): # Pieprasām lietotājam ievadīt datus
        print('ievadiet',i+1,'. skolēna datus:')
        vards = input("Ievadi vārdus: ")
        uzvards = input("Ievadi uzvārdus: ")
        klase = input("Ievadi klases: ")
    # Ieraksta datus CSV failā
    rakstitajs.writerow([vards, uzvards, klase])

