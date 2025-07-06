from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("personaGastosSinTarjetaCredito").getOrCreate()
rdd= spark.sparkContext.textFile("casoDePrueba1.txt")
rdd1 = rdd.map(lambda l :l.split(";"))
rdd1 = rdd1.map(lambda x :(x[0], 0 if x[1].strip().lower() == "tarjeta de crédito" else int (x[2])))
rdd1 = rdd1.reduceByKey(lambda a, b: a+b)
rdd1 = rdd1.map(lambda x :f"{x[0]};{x[1]}")
rdd1.saveAsTextFile("salida")