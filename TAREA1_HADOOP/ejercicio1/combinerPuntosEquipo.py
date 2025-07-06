import sys
from collections import defaultdict

conteo_local = defaultdict(int)
for linea in sys.stdin:
    linea = linea.strip()
    equipo, puntaje = linea.split("\t", 1)
    conteo_local[equipo] += int(puntaje)

for equipo in conteo_local:
    print(f"{equipo}\t{conteo_local[equipo]}")
