#is
x= y =[1, 2, 3]
z= [8,7,5]

print(x==y)
print(x==z)
print(x is y)
print(x is z)

a = [1,2,3]
b= [2,4]
del a[2]
b[1] = 1
b.reverse()
print(a == b)
print(a is b)

#in
x = ['apple', 'banana']
print('banana'in x)

name ='ali'
print('a' not in name)