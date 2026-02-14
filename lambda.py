# def square(num): return num ** 2

numbers = [1,2,3,4,5,6,7,8,9]

# result = list(map(square, numbers))

# for item in map(square, numbers):
#     print(item)

# square = lambda num: num ** 2
# result = list(map(square, numbers))
# result = square(3)
# print(result)

#*************** 1. YOL ******************
def check_even(num): return num % 2 == 0
result = list(filter(check_even, numbers))
print(result)


#*************** 2. YOL ******************
def check_even(num): return num % 2 == 0
result = list(filter(lambda num: num%2 == 0, numbers))
print(result)

#*************** 3. YOL **********************
check_even: lambda num:  num % 2 == 0
result = list(filter(check_even, numbers))
print(result)

#**************** 4. YOL **********************
check_even: lambda num:  num % 2 == 0
result = check_even(numbers[2])
print(result)
