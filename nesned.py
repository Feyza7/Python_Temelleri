# def greeting(name):
#     print('helloo ',name)

# print(greeting('feyza'))
# print(greeting)

# sayHello = greeting # bir objeyi birbirlerine atama yapıldığında bilginin
#                     # tutulduğu adrese atama yapılır

# print(sayHello)
# print(greeting)

# print(greeting('asd'))
# print(sayHello) # ikisi de aynı şeyidir

#encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1+1
#     num2 = inner_increment(num1)
#     print(num1,num2)

# outer(10)
#inner_increment(10) çağırılamaz çünkü outer()'a bağlı

def factorial(number):
    if not isinstance(number, int): #isinstance() => number integer mi kontrol ediyor
        raise TypeError("number must be an integer")
    
    if number < 0:
        raise ValueError("number must be zero or positive")


    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number-1)
    
    return inner_factorial(number)

print(factorial(-5))
    


