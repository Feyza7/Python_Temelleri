number = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(number)
val = max(number)
val = max(letters)
val = min(letters)

val = number[3:6]
val = number[:3]
val = number[4:]
print(val)

number[4] = 40
number.append(77) #listenin sonuna eleman ekleme
number.insert(3,78) #üçüncü indeksten sonra eleman ekleme
number.insert(-1,13)
number.pop() #sondaki elemanı siler
number.remove(16) #16'yı siler
number.sort() #küçükten büyüğe sıralar
letters.sort()
number.reverse()
letters.reverse()

print(number)
print(letters)

print(len(number))
print(len(letters))

print(number.count(10))
print(letters.count('a'))

number.clear()
print(number)