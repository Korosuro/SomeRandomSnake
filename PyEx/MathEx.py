import random 
import math 

print ("Hello world!")

a = random.randint(1,100)
b = random.randint(1,100)
txt = "{} is bigger than {}"
txt2 = "{} is smaller than {}"

if a == b:
    print ("Random numbers were generated equally, please repeat")
elif a > b:
    print (txt.format(a,b))
elif a < b:
    print (txt2.format(a, b))
    
