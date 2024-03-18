from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JogosBanidos").getOrCreate()

# load data

data_games_banned = "data/games_banned.csv"
df = spark.read.csv(data_games_banned, header=True, inferSchema=True)

# data view"
df = df.fillna("Vazio")
# Remove Duplicates
df = df.dropDuplicates()
#df.show()
df = df.select("Id","Country","Developer","Genre")

df = df.withColumnRenamed("Id","Jogo")
df = df.withColumnRenamed("Country","Pais")
df = df.withColumnRenamed("Developer","Desenvolvedor")
df = df.withColumnRenamed("Genre","Genero")

#df.show()

df_filtrado = df.filter(df["Pais"] == "Brazil")
#df_filtrado.show()

#Order data

df_ordenado = df.orderBy(df["Pais"] == "Brazil")
df_ordenado.show()
