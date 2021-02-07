import string
import numpy as np
import matplotlib.pyplot as plt
f = open("dati.txt", 'r')
print(f.readline())
valori = str(riga)
coordX = []
coordY = []
for riga in f:
  valori = str(riga)
  Nval = len(valori)
  valori = valori.strip('\n')
  valori = valori.split(',')
  valori = list(valori)
  print(valori)
  coordX.append(int(valori[0]))
  coordY.append(int(valori[1]))
f.close()
print ("X: ",coordX)
print ("Y: ",coordY)
coordX.sort()
coordY.sort()
print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)
print(type(coordX))
print(type(coordY))
plt.plot(coordX,coordY)
plt.ylabel('some numbers')
plt.show()