# Error

# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

# Error Handling

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print('hatalı değer girdiniz')
#     print(e)


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('hatalı değer girdiniz')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('hatalı değer girdiniz',ex)
    else:
        break
    finally:
        print('try except sonlandı.')
    

