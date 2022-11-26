#!/usr/bin/env python3
import os

m1 = list()
m2 = list()
m3 = list()

def multiplicacion(a, b):
    ret = list()
    for f in range(len(a)):
        for c in range(len(b[f])):
            ret.append(list())
            suma = 0
            for m in range(len(a[f])):
                suma = a[f][m] * b[m][c]
            ret[c].append(suma)
    return ret

f1 = int(input("Filas de la primera matriz: "))
c1 = int(input("Columnas de la primera matriz: "))
f2 = int(input("Filas de la segunda matriz: "))
c2 = int(input("Columnas de la segunda matriz: "))

if c1 != f1:
    print("Columnas de la primera y filas de la segunda matriz no coinciden")
    os._exit(1)

for f in range(f1):
    m1.append(list())
    for c in range(c1):
        val = float(input(f"Valor ({f},{c}): "))
        m1[f].append(val)

for f in range(f2):
    m2.append(list())
    for c in range(c2):
        val = float(input(f"Valor ({f},{c}): "))
        m2[f].append(val)

m3 = multiplicacion(m1,m2)

for f in range(f1):
    print("[ ", end="")
    for c in range(c1):
        print(m1[f][c], end=", ")
    print("]")

for f in range(f2):
    print("[ ", end="")
    for c in range(c2):
        print(m2[f][c], end=", ")
    print("]")

for f in range(len(m3)):
    print("[ ", end="")
    for c in range(len(m3[f])):
        print(m3[f][c], end=", ")
    print("]")

