#import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")

print("Tamanho do df", df.size)

mean_df = df['windspeed'].mean()
print("média da coluna windspeed", mean_df)

mean_df = df['temp'].mean()
print("média da coluna temp", mean_df)

print("registros existem para o ano de 2011 - 0 e 2012 - 1\n", df['year'].value_counts() )

count_total = df.groupby('year').sum().filter(["year", "total_count"])
df['year'] = df.groupby('total_count')['total_count'].transform('count').filter(["year", "total_count"])
print("totais de alugueis de bicicleta por ano: \n",count_total)
#print(df.head(10))
#print(df.shape)
#print(df.describe())

mean_estações = df.groupby('season').mean().filter(["season", "total_count"])
print("média por estação: \n",mean_estações)

mean_horario= df.groupby('hour').mean().sort_values(["total_count","hour"],
    ascending=True).filter(["hour", "total_count"])
print("média de locação por horário:\n ",mean_horario)

mean_horario_semana= df[(df['weekday']=='3')].groupby('weekday').mean().sort_values(["total_count","hour"],
    ascending=True)
print("média de locação por horário semana:\n ",mean_horario_semana)