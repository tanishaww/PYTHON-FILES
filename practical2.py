# swap two numbers

# a=int(input("Enter number 1: "))
# b=int(input("Enter number 2: "))
# print("Before swapping number 1: ",a)
# print("Before swapping number 2: ",b)
# x = a
# a = b
# b = x 
# print("After Swapping number 1: ",a)
# print("After swapping number 2: ",b)

# permutation:

# from itertools import permutations
# l = list(permutations(range(1,4)))
# print(l)

# union and intersection:

# str1 = 'hello'
# str2 = 'hell'

# result = ''

# for char in str1:
#     if char in str2 and not char in result: 
#         result += char
    
# print(result)

# result = set(str1).intersection(str2)

# resultstr = ''.join(result)

# print(resultstr)

#prime number

# a = int(input("Enter the lower limit: "))
# b = int(input("Enter the upper value: "))
# print("The prime numbers in the range are: ")
# for number in range(a,b+1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#             else:
#                 if print(number):


# factorial

# def fact(n):
#     if n <= 1:
#         return n
#     return n*fact(n-1)
# b = int(input("Enter the number: "))
# a = fact(b)
# print(a)


def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

a= int(input("Enter a Number: "))
for j in range(2,a+1):
    if (prime(j)):
        print(j)
