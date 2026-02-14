list = [1, 2, 3]

tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(list[1])
print(tuple[1])

print(len(list))
print(len(tuple))

list = ['ali', 'veli']
tuple = ('damla', 'ayşe')
names = ('demet', 'emel', 'ayşe') + tuple

list[0] = "ahmet"
# tuple[0] = "mehmet" atama işlemi olmaz

print(list)
print(tuple)
print(names)
