# YÖNTEM 1

# import math 
# import math as islem

# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = islem.factorial(3)


# YÖNTEM 2

# from math import *

def sqrt(x):                 # eğer importun altında tanımlansaydı
    print('x: '+ str(x))     # bu fonksiyon çalışacaktı

from math import factorial, sqrt, ceil

value = factorial(5)
value = sqrt(9)

print(value)