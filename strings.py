name = "Ali"
surname = "Yılmaz"
age = 99
greeting = 'My name is ' + name + ' ' + surname + ' and\nI am ' + str(age) + ' years old.'
lenght = len(greeting)
print(greeting)
print("5.karakter: ", greeting[5])
print("karakter sayısı: ", lenght)
print("son karakter:", greeting[lenght-1])
print("son karakter:", greeting[-1])
print("3'teen 7. karaktere kadar: ", greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:2]) #2den başla 40a kdar git 2şer 2şe
