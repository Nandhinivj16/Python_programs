def greet():
    print("Hello! Welcome to the program.")

greet()   

def greet(name):#name-parameter
   print("hello" + name)

greet("nandy") #passing arguments
print("vijay")
greet("ganesh")  

def sum(num):
    result=num/2
    return result
print(sum(10))

def sum(num1,num2):
    result=num1+num2
    return result
print(sum(10,20))

def result(*arg):#args packed in tuple
    sum=0
    for i in arg:
      sum=sum+i
    return sum
print(result(10,20,30,40,50))


def print_addr(**kwargs): #packs all keyword arguments into a dictionary
   for key,val in kwargs.items():
      print(val)


print_addr(door_no="93",street_name="rr nagar",city="chennai")   