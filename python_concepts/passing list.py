def print_list(list):
    for i in list:
        print(i.title())
name=["nandy","vijay","vikram","adithi"]        
print_list(name)

#modules(import.func)

# exception handling
try:
  num = int(input("enter a numerator: "))
  den = int(input("enter a denominator: "))
  result =num/den
  print(result)

except ZeroDivisionError as e:
   print(e)
   print("you cannot divide by zero...")
except ValueError:
   print("Enter numbers onlty..")
  
except Exception:
   print("some error")

print("bye")