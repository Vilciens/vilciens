aa = {
  "Audi": 2009,
  "Golfs": 2007,
  "Toyota": 2005,
  "Tesla": 2022,
  "Bembis": 2004,
    #keys ir vārdi
}
x=aa.keys() #ja gribi ar cipariem neraksti . keys
print(x)
y=aa.values()
print(y)
for aa, year in aa.items():
  print(aa,year)
if'Audi' in aa:
  print('audi nav vardnica')
else:
  print('audi ir vardnica')
