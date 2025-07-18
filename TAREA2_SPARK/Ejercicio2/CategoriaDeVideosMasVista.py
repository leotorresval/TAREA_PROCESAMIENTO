from pyspark.sql import SparkSession
import sys
import os
spark =SparkSession.builder.appName("CategoriaDeVideosMasVista").getOrCreate()
entrada = sys.argv[1]
salida = sys.argv[2]
archivos = [os.path.join(entrada, f) for f in os.listdir(entrada) if f != "log.txt"]
rdd = spark.sparkContext.textFile(",".join(archivos))
rdd = rdd.map(lambda x: x.strip().split("\t"))
rddCompleto = rdd.filter(lambda x : len(x)>=6)
rdd1 = rddCompleto.map(lambda x: (x[3],int(x[5])))
rdd1 = rdd1.reduceByKey(lambda x,y: x+y)
rdd1 = rdd1.sortBy(lambda x : x[1],ascending=False)
categoriaMaxima = rdd1.take(1)
df = spark.createDataFrame(categoriaMaxima, ["categoria", "totalVistas"])
df_txt = df.selectExpr("concat(categoria, ';', totalVistas) as linea")
df_txt.write.mode("overwrite").text("salida_"+salida+"/")
