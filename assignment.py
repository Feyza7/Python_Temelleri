x, y, z = 5, 10, 20

x, y = y, x

x += 5
x -= 5
x *= 5
x /= 5
x %= 5
y //= 5 #tam kısmı bölme
y **= 5 #üs alma

print(x, y, z)

values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values

print(x, y, z)