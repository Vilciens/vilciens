aa = {
  "Anna": 5,
  "Rainers": 4,
  "Timijs": 6,
  "Mareks": 9,
  "Mārtiņš": 7, #keys ir vārdi
}
x=aa.keys() #ja gribi ar cipariem neraksti . keys
print(x)
y=aa.values()
print(y)
z=aa.get('Mārtiņš')
print(z)