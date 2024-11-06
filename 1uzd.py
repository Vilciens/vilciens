import csv

with open('atskaite-liepja.csv', 'r', encoding = 'utf-8'):
    lasītājs = csv.reader(fails, delimiter=';')
    van_count = 0
    next (lasītājs) 
    rinfu_skaits=sum(1 for rinda in lasītājs)
print(f'Failā ir{rindu_skaits}rindas')

