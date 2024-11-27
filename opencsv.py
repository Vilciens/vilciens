import csv
from collections import Counter
novads_counter=Counter()
try:
    with open('veseliba.csv', mode='r', newline='',encoding='utf-8 ') as file:
        reader=csv.reader(file)
        header=next(reader)
        for row in reader:
            if len(row)>1:
                novads=row[1].strip()
                novads_counter[novads] +=1
    most_common_novads=novads_counter.most_common(1)
    print('Novads kurš visvairāk atkārtojas:')
    for novads, count in most_common_novads:
        print(f'{novads}: {count} reizes')
except FileNotFoundError:
    print("Fails 'veseliba.csv' netika atrasts. Pārbaudi faila atrašanās vietu.")
except Exception as e:
    print(f"Kļūda: {e}")