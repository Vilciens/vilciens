import csv

with open('veseliba.csv', mode='r', newline='',encoding='latin-1 ') as file:
    reader=csv.reader(file)
    for row in reader:
        novads=row[0]
        pagasts=row[1]
        dzimte=row[2]
        gadi=row[3]

        novads
