#!/usr/bin/python3

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

subproblema = None
tiendas = set()

for claveValor in sys.stdin:
    cliente, tienda = claveValor.strip().split("\t", 1)

    if subproblema is None:
        subproblema = cliente

    if subproblema == cliente:
        tiendas.add(tienda)
    else:
        for numTiendaVisitada in range(0, len(tiendas),1):
            tiendaVisitada = tiendas.pop()
            print("%s\t%s" % (subproblema, tiendaVisitada))

        subproblema = cliente
        tiendas = set()
        tiendas.add(tienda)

for numTiendaVisitada in range(0, len(tiendas),1):
    tiendaVisitada = tiendas.pop()
    print("%s\t%s" % (subproblema, tiendaVisitada))
