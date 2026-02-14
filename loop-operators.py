#range
# for i in range(3,15,2):
#     print(i)

# print(list(range(3,15,2)))

#enumerate

greeting = 'Hello'
index = 0

for letter in greeting:
    print(f"index: {index}, letter: {greeting[index]}")
    index += 1


print("*"*50)

for index, item in enumerate(greeting):
    print(f'index: {index}, letter: {item}')

#zip
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)