from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("personaYMetodosDePago").getOrCreate()

rdd = spark.sparkContext.textFile("casoDePrueba3.txt")
rdd = rdd.map(lambda x:x.split(";"))
rddMayores = rdd.map(lambda x: (x[0],1 if x[1].strip().lower() == "tarjeta de crédito" and int(x[2])>1500 else 0))
rddMayores = rddMayores.reduceByKey(lambda x,y: x+y)
rddMayores = rddMayores.map(lambda x: f"{x[0]};{x[1]}")
rddMayores.saveAsTextFile("comprasConTDCMayorDe1500")
rddMenores = rdd.map(lambda x: (x[0],1 if x[1].strip().lower() == "tarjeta de crédito" and int(x[2])<=1500 else 0))
rddMenores = rddMenores.reduceByKey(lambda x,y: x+y)
rddMenores = rddMenores.map(lambda x: f"{x[0]};{x[1]}")
rddMenores.saveAsTextFile("comprasConTDCMenoroIgualDe1500")