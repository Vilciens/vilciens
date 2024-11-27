import csv

with open('todo_list.csv', mode='w', newline='') as file:
    dati = csv.writer(file)
    dati.writerow(["Uzdevums"])
    while True:
        uzdevums = input("Ievadiet uzdevumu: ")
        dati.writerow([uzdevums])
        jauns_uzd = input("Vai vēlaties pievienot vēl uzdevumu? (jā/nē): ")
        if jauns_uzd.lower() != "jā":
            break