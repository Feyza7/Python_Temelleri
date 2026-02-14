fruits = {'orange' , 'apple', 'banana'}
#print(fruits[0]) indekslenemez

fruits.add('cherry')
fruits.update(['mango','grape'])

fruits.remove('mango')
fruits.discard('apple')

fruits.pop() #sıralı olmadığı için sondaki elemanı silmeyebilir
fruits.clear()

print(fruits)

myList = [1, 8, 9, 5, 4, 1, 6, 8]
print(set(myList)) #tekrarlananları siler
print(myList)
