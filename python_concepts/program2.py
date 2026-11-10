name= "Dear Anand,"
leave= "you have 15 days of leave balance for this"
year="year(2021)"
print(name+ " " +leave + "\n" + year)


#2.assignment
name=input("user name: ")
print("username: "+ name)
email=input("email: ")
print("email: "+ email)
number=input("ph: ")
print("ph: " +number)

#3.assigbnment
import math
num=input("print a number: ")
num1=int(num)
print(num1)
print(math.log2(num1))
print(math.cos(num1))
print(math.exp(num1))


import random
num=random.randint(1,20)

guess=int(input("can you guess the number between 1 to 20: "))

while num != guess:
    if guess<num:
        print("your guess is too low" )
    else: 
        print("your guess is too high")
    guess=int(input("guess again: "))    
print("you won the game")        
