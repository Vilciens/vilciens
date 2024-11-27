#uzd3
import csv

with open('augli.csv', 'w', newline='', encoding='utf-8') as fails:
    rakstitajs = csv.writer(fails)
    rakstitajs.writerow(['nosaukums', 'cena', 'svars'])
    for i in range(3):
        print('ievadiet',i+1,'. augļa datus:')
        nosaukums = input("Ievadi augļa nosaukumu: ")
        cena = input("Ievadi augļa cenu: ")
        svars = input("Ievadi augļa svaru: ")
        rakstitajs.writerow([nosaukums, cena, svars])



