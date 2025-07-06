import sys

for linea in sys.stdin:
    linea = linea.strip()
    try:
        num,Season,Game,Score,Teams,local,visitante = linea.split(",")
        e1,e2= Score.split("-")
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
        print("%s\t%s" % (local+"_Local",e1))
        print("%s\t%s" % (visitante+"_Visitante",e2))
    except:
        continue    
