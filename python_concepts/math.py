import math
num=int(input("enter a number: "))
print(num)
result=math.factorial(num)
print(result)

num1=int(input("enter another number: "))
print(num1)
for i in range (1,num+1):
    if num % i== 0:
     print(i)

