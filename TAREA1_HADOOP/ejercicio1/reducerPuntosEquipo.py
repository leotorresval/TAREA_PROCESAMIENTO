import sys
subproblema =None
puntos = 0

for linea in sys.stdin:
    linea=linea.strip()
    equipo, puntaje =linea.split("\t",1)
    puntaje = int(puntaje)
    
    if subproblema==None:
        subproblema=equipo
    
    if subproblema==equipo:
        puntos = puntos+puntaje
    else:
        print(f"{subproblema};{puntos}")
        subproblema=equipo
        puntos=puntaje
if subproblema is not None:
    print(f"{subproblema};{puntos}")
    
    
    