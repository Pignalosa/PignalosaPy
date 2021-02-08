from random import randint
f = open("dati4.txt", 'w')
dati= ""
for riga in range(10):
    for elemento in range(1):
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
        dati = dati + "\n"
print(dati)
f.write(dati)
f.close()