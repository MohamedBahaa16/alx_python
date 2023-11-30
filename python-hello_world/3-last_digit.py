import random
number = str(random.randint(-1000,1000))
if int(number[-1:]) > 5: 
   print(f"It is {number[-1:]} and is greater than 5 ")
elif int(number[-1:]) == 0:
   print(f"It is{number[-1:]} and is zero")
else:
    print(f"The {number[-1:]} is less than 6 and is less than 6 and not 0")



