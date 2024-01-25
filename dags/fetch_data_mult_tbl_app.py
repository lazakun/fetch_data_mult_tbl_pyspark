from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
import os
import sys
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import lit


appName = "PySpark SQL Server to PostGres - via JDBC"
master = "spark://Lazlo.:7077"
conf = SparkConf() \
    .setAppName(appName) \
    .setMaster(master) \
    .set("spark.driver.extraClassPath","/home/lazlo/jdbc_jars/*") \
    .set("spark.executor.extraClassPath","/home/lazlo/jdbc_jars/*") \

sc = SparkContext.getOrCreate(conf=conf)

spark = SparkSession(sc)

spark

target_url = "jdbc:postgresql://192.168.100.4:5432/dvdrental?user=potey&password=lazlo"
#target_driver = "org.postgresql.Driver"
source_url = "jdbc:sqlserver://192.168.100.4;databaseName=AdventureWorks2019;user=potey;password=lazlo;encrypt=true;trustServerCertificate=true;"

sql = """select  t.name as table_name from sys.tables t 
where t.name in ('Employee_Buyer','Employee_Janitor','Employee_Prod_Tech','Employee_Sales_Rep') """

file = open("/home/lazlo/jdbc_jars/script.txt", "r")
script = file.read()

dfs=spark.read. \
    format("jdbc"). \
    options(url=source_url, query=sql). \
    load()

data_collect = dfs.collect()
# looping thorough each row of the dataframe
for row in data_collect:
    # while looping through each
    # row printing the data of table_name
    print(row["table_name"])

table_name_var = row["table_name"]

tbl_name = row["table_name"]
dest_df = spark.read \
    .format("jdbc") \
    .option("url", source_url) \
    .option("query", "select top 1 * from dbo." + table_name_var) \
    .load()
dest_df = dest_df.withColumn("table_name", lit(table_name_var))

dest_df = dest_df.limit(0)

for row in data_collect:
    table_name_var = row["table_name"]
    src_df = spark.read \
        .format("jdbc") \
        .option("url", source_url) \
        .option("query", "select * from dbo." + table_name_var + ' ' + script) \
        .load()
    src_df = src_df.withColumn("table_name", lit(table_name_var))
    dest_df = dest_df.union(src_df)

dest_df.write.mode("overwrite") \
    .format("jdbc") \
    .option("url", target_url) \
    .option("dbtable", "employee_output_airflow") \
    .save()

spark.stop()