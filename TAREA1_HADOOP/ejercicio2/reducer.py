#!/usr/bin/ python3
import sys
subproblema =None
puntos = 0
contador = 0
for linea in sys.stdin:
    linea=linea.strip()
    equipo, puntaje =linea.split("\t")
    puntaje = int(puntaje)
    
    if subproblema==None:
        subproblema=equipo
    
    if subproblema==equipo:
        puntos = puntos+puntaje
        contador +=1
    else:
        total=puntos/contador
        total= round(total)
        e,u = equipo.split("_")
        print(e,";",u,";",total)
        subproblema=equipo
        puntos=puntaje
        contador=1
    
    
    
    
