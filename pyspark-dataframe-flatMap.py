# -*- coding: utf-8 -*-
"""
author nubeera.com
"""


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('nubeera.com').getOrCreate()

columns = ["name","languagesAtSchool","currentState"]
data = [("James,,Smith",["Java","Scala","C++"],"CA"), \
    ("Michael,Rose,",["Spark","Java","C++"],"NJ"), \
    ("Robert,,Williams",["CSharp","VB"],"NV")]

df = spark.createDataFrame(data=data,schema=columns)
df.printSchema()
df.show(truncate=False)

#Flatmap    

