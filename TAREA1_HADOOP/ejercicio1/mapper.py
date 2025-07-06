#!/usr/bin/ python3
import sys

for linea in sys.stdin:
    linea = linea.strip()
    try:
        num,Season,Game,Score,Teams,local,visitante = linea.split(",")
        e1,e2= Score.split("-",2)
        e1= int(e1)
        e2 = int(e2)
        if local=="Deportivo Alavés":
            local="Alavés"
        if visitante=="Deportivo Alavés":
            visitante="Alavés"
        if local=="R. Sociedad":
            local="Real Sociedad"
        if visitante=="R. Sociedad":
            visitante="Real Sociedad"
        if e1>e2:
            print("%s\t%s" % (local,3))
        elif e1==e2:
            print("%s\t%s" % (local,1))
            print("%s\t%s" % (visitante,1))
        else:
            print("%s\t%s" % (visitante,3))    
    except:
        continue    