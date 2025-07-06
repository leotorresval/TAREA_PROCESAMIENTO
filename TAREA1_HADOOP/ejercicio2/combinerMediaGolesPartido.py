import sys
from collections import defaultdict

datos = defaultdict(lambda: [0, 0])

for linea in sys.stdin:
    linea = linea.strip()
    equipo, puntaje = linea.split("\t")
    puntaje = int(puntaje)
    datos[equipo][0] += puntaje
    datos[equipo][1] += 1

for equipo in datos:
    suma, contador = datos[equipo]
    print(f"{equipo}\t{suma},{contador}")
