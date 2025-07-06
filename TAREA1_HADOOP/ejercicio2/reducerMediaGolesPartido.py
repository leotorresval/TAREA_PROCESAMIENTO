import sys
subproblema =None
puntos = 0
contador = 0
for linea in sys.stdin:
    linea=linea.strip()
    equipo, puntaje =linea.split("\t")
    puntaje , c = puntaje.split(",")
    puntaje = int(puntaje)
    c = int(c)
    if subproblema==None:
        subproblema=equipo
    
    if subproblema==equipo:
        puntos = puntos+puntaje
        contador +=c
    else:
        total=puntos/contador
        total= round(total,2)
        e,u = subproblema.split("_")
        print(e,";",u,";",total)
        subproblema=equipo
        puntos=puntaje
        contador=c
    
if subproblema is not None:
    total=puntos/contador
    total= round(total,2)
    e, u = subproblema.split("_")
    print(e,";",u,";",total)
    
    
