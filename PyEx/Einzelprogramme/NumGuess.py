#Random Number, higher-lower, attempt-counter

import random

a = random.randint(1,50)
c = 0
counter = 0

while a != c:
    b = int(input("Welche Zahl ist gesucht? "))
    if b < a:
        print ("Zu wenig!")
        counter += 1
    elif b > a:
        print ("Zu hoch!")
        counter += 1
    elif b == a:
        print ("Korrekt!")
        counter += 1
        print ("Anzahl der Versuche: {}".format(counter))
        break