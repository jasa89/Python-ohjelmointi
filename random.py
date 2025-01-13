from random import randint

print("Heitetään kolikkoa viidesti:")

i=0

while i<5:
    i+=1
    kolikko=randint(0,1)
    if kolikko==0:
        print("klaava!")
    else:
        print("kruuna!")