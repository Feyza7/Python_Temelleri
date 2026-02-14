message = 'Hello There. My name is Ali Yılmaz'

message = message.upper()
print(message)

message = message.lower()
print(message)

message = message.title()
print(message)

message = message.capitalize()
print(message)

x = " herkese merhaba, insanlar"

x = x.strip()
print(x)

x = x.split(',')
print(x)
print(x[1])

x = '*'.join(x)
print(x)

index = message.find('ali')
print(index)

isFound = message.startswith('H')
print(isFound)

isFound = message.endswith('z')
print(isFound)

message = message.replace('ali' , 'Ali')
print(message)

message = message.replace(' ' , '*').replace('e' , '-')
print(message)

message = message.center(100)
print(message)

"""
message = message.center(50,'*')
print(message)
"""
