#1Nolasīt un izvadīt konsolē faila data.json saturu.
import json
with open('data.json','r')as fails:
    rez=json.load(fails)

print(rez)

#2Python vardnicas datus saglabāt json formatā
import json
mani_dati= {
    'name':'snoop dawg',
    'age':40,
    'email':'snoop dawgis here dawng'
}

with open('jaunie_dati.json','w')as fails:
    json.dump(mani_dati,fails,indent=2)

#3Uzrakstiet Python skriptu, kas izveido JSON failu ar sekojošiem datiem
import json
data= {
    'name':'snoop dawg',
    'age':40,
    'email':'what is tuple',
    'hobbies':['reading','hiking','photographing']
}
with open('user_data.json','w')as fails:
    json.dump(data,fails,indent=2)

#4Nolasiet JSON failu produkti.json ar produktu sarakstu un izvadiet visus produktus, kuru cena ir zemāka par 10 EUR.

import json
with open('produkti.json','r',encoding='utf-8')as fails:
    data=json.load(fails)

print('produkti,kuru cena ir zemaka nekā 10 euro:')
for product in data ['products']:
    if product['price']<10:
        print(product['name'],':',product['price'],'eur')

#5lai tikai radītos piena, un maize cenas

import json
with open('produkti.json','r',encoding='utf-8')as fails:
    data=json.load(fails)

print('produkti,kuru cena ir zemaka nekā 10 euro:')
for product in data ['products']:
    if product['name']=='Maize' or product['name']=='Piens':
        print(product['name'],':',product['price'],'eur')

#6 Nolasiet JSON failu un izvadiet visu informāciju par augļiem. Izmantot JSON failu fruit.json.
import json
with open('fruits.json','r')as f:
    data=json.load(f)

print(f'informacija pa augli: {data}')

#7Izveidojiet jaunu Python vārdnīcu, kurā glabājas informācija par augļiem un saglabājiet to jaunā JSON failā.
import json
fruit_data={
    'fruit':'apple',
    'size':'large',
    'color':'red',

}

with open('fruit.json','w',encoding='utf-8')as fails:
    json.dump(fruit_data, fails,indent=4)


#8Pārbaudiet, vai JSON failā ir atribūts "taste". Ja ir, izvadiet tā vērtību, ja nav, izvadiet ziņojumu "Atribūts 'taste' nav atrasts".
import json
with open('fruit.json','w',encoding='utf-8')as fails:
    j
    data=json