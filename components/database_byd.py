from matplotlib.pyplot import show
import sqlite3
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


df = pd.read_sql_query("SELECT * FROM EnergyConsumption", sqlite3.connect('./data/database_byd.db'))
#tiempo de viaje mas largo
trip_long=(df["duration"].max())
#viaje mas largo
trip_average=(df["trip"].max())
#viaje promedio
trip_mean=(df["trip"].mean())
#kilometros totales
trip_km_total=(sum(df["trip"]))
#gasto total combustible
fuel_total=(sum(df["fuel"]))
#gasto medio combustible
fuel_mean=((df["fuel"].mean()))
#fuel consumido por meses
fuel_sum_month=(df.groupby(['month']).count()['fuel'])
#gasto_total combustible
fuel_total=((df["fuel"].count()))
#gasto combustible a los 100
fuel_km_100= ((fuel_total/trip_km_total)*100)
#porcentaje viajes solo electrico en porcentaje
trip_fuel_up=((df["fuel"]==0).value_counts(True))
#media gasto electricidad
elec_mean=((df["electricity"]>0).mean())

print (df.describe(include='object'))
print (elec_mean)
print (df.head())
