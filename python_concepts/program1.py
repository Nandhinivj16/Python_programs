name=input("what is your name: ")
print("hello" + " " + name)
weight=input("what is your weight: ")
print("your weight is: " + weight)
height=float(input("what is your height: "))
print(type(height))
print("you are "+str(height/2.54) + "inches tall")

height_inches="{:.2f}".format(height/2.54)#string.format()method
print("you are "+height_inches + "inches tall")