#!/usr/bin/env python3
import os
import random
import time

m1 = list()
m2 = list()
m3 = list()

def multiplicacion(a, b):
    ret = list()
    for f in range(len(a)):
        ret.append(list())
        for c in range(len(b[f])):
            suma = 0
            for m in range(len(a[f])):
                suma += a[f][m] * b[m][c]
            ret[f].append(suma)
    return ret

f1 = int(input("Filas de la primera matriz: "))
c1 = int(input("Columnas de la primera matriz: "))
f2 = int(input("Filas de la segunda matriz: "))
c2 = int(input("Columnas de la segunda matriz: "))

if c1 != f2:
    print("Columnas de la primera y filas de la segunda matriz no coinciden")
    os._exit(1)

for f in range(f1):
    m1.append(list())
    for c in range(c1):
        val = random.randint(1,50)
        m1[f].append(val)

for f in range(f2):
    m2.append(list())
    for c in range(c2):
        val = random.randint(1,50)
        m2[f].append(val)

inicio = time.time()
m3 = multiplicacion(m1,m2)
fin = time.time()
print("El tiempo es:", fin-inicio,"segundos")

