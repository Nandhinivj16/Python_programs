num=30
if num%10==0:
    print(str(num) + " is divisible by 10")
else:
    print(str(num) + " is not divisible by 10")    

# elif ladder
num1 = 40

if(num1>50):
    print("number is greater than 50")
elif(num1<50): 
    print("number is less than 50")
else:
    print("number is invalid")    


 #nestedif statement  
 #logical operators  
num3=int(input("enter a num: ")) 
if num3>99 and num3<1000:
    if num3%2==0:
        print(str(num3) + " is a three digit even number")
    else:
        print(str(num3) + " is a three digit odd number")
else:
    print("number is not a three digit number")
#bitwise operators

print(3 & 4)
print(3 | 4)
print(3^4)
print(12<<2)
print(12>>2)    
