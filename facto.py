def fact(n):
    if n <= 1:
        return n
    return n*fact(n-1)
b = int(input("Enter the number: "))
a = fact(b)
print(a)

a = int(input("Enter the number: "))
fact = 1
for i in range(1,a+1):
    fact = fact*i
print(fact)