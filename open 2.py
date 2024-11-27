import csv

with open('atrapalīdzība.csv', 'r') as fails:
    lasītājs = csv.reader(fails)
    for rinda in lasītājs:
        print(rinda)