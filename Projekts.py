import csv
from collections import Counter
novads_counter = Counter()
dzimte_counter = Counter()
vecums_counter = Counter()
pagasts_counter = Counter()
try:
    with open('veseliba.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if len(row) > 1:
                novads = row[1].strip()
                dzimte = row[2].strip()
                vecums = row[3].strip()
                pagasts = row[4].strip()
                novads_counter[novads] += 1
                dzimte_counter[dzimte] += 1
                vecums_counter[vecums] += 1
                pagasts_counter[pagasts] += 1
most_common_novads = novads_counter.most_common(1)
print('Novads, kurš visvairāk atkārtojas:')
for novads, count in most_common_novads:
    print(f'{novads}: {count} reizes')
most_common_dzimte = dzimte_counter.most_common(1)
print('\nDzimte, kurš visvairāk atkārtojas:')
for dzimte, count in most_common_dzimte:
    print(f'{dzimte}: {count} reizes')
most_common_vecums = vecums_counter.most_common(1)
print('\nVecums, kurš visvairāk atkārtojas:')
for vecums, count in most_common_vecums:
    print(f'{vecums}: {count} reizes')
most_common_pagasts = pagasts_counter.most_common(1)
print('\nPagasts, kurš visvairāk atkārtojas:')
for pagasts, count in most_common_pagasts:
    print(f'{pagasts}: {count} reizes')
except FileNotFoundError:
print("Fails 'veseliba.csv' netika atrasts, pārbaudi faila atrašanās vietu.")
except Exception as e:
print(f"Kļūda: {e}")