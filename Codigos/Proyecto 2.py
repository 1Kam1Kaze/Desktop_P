print('\n------------------------------------------------------------------------------------\n')

#Librerias utilizadas. 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

#Lectura del archivo.
d1 = pd.read_csv('/Archivos/AlarmasSistema.csv', sep=';')
datos = pd.DataFrame(d1)
print(datos)
st.header('Lectura del archivo')
st.write(datos)

print('\n------------------------------------------------------------------------------------')

#Calcular la cantidad de alarmas generadas por cada nivel de severidad.
severidad_counts = datos['SEVERITY'].value_counts()
print(f'\nContador de severidad por nivel: {severidad_counts}')

print('\n------------------------------------------------------------------------------------')

#Identificar severidad mas frecuente.
severidad_mas_frecuente = severidad_counts.idxmax()
print(f'\nSeveridad mas frecuente: {severidad_mas_frecuente}')

print('\n------------------------------------------------------------------------------------')

#Promedio y desviacion estandar de la severidad de las alarmas.
promedio_severidad = datos['SEVERITY'].mean()
desviacion_estandar_severidad = datos['SEVERITY'].std()
print(f'\nPromedio: {promedio_severidad}')
print(f'\nDesviacion estandar: {desviacion_estandar_severidad}')

print('\n------------------------------------------------------------------------------------')

#Obtener el Top 5 de los elementos que mas alarmas tienen segun severidad.
top_5_elementos = datos['NAME'].value_counts().head(5)
print(f'Top 5 elementos: {top_5_elementos}')

print('\n------------------------------------------------------------------------------------')

#Calcular la duracion promedio de las alarmas (diferencia entre la hora de inicio y la hora de cancelacion).
datos['DURATION'] = pd.to_datetime(datos['CANCEL_TIME']) - pd.to_datetime(datos['ALARM_TIME'])
promedio_duracion = datos['DURATION'].mean()
print(f'\nPromedio duracion: {promedio_duracion}')

print('\n------------------------------------------------------------------------------------')

#Identificar las alarmas con mayor y menor duracion.
alarma_mayor = datos.loc[datos['DURATION'].idxmax()]
alarma_menor = datos.loc[datos['DURATION'].idxmin()]
print(f'Alarma mayor: {alarma_mayor}\n')
print(f'Alarma menor: {alarma_menor}')

print('\n------------------------------------------------------------------------------------')

#Relacionar la duracion de las alarmas con su severidad.
print(f'\n{datos.groupby("SEVERITY")["DURATION"]}')

print('\n------------------------------------------------------------------------------------')

#Analisis de la cantidad de alarmas registradas por hora del dia, dia de la semana o mes, para identificar picos de actividad.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['hour'] = datos['ALARM_TIME'].dt.hour
datos['day_of_week'] = datos['ALARM_TIME'].dt.day_name()
datos['month'] = datos['ALARM_TIME'].dt.month
alarms_by_hour = datos.groupby('hour').size()
print(f'\n{alarms_by_hour}')
alarms_by_day = datos.groupby('day_of_week').size()
print(f'\n{alarms_by_day}')
alarms_by_month = datos.groupby('month').size()
print(f'\n{alarms_by_month}')
#Comparar el comportamiento temporal de las alarmas en distintas severidades.
alarms_by_severity_hour= datos.groupby(['hour', 'SEVERITY']).size().unstack().fillna(0)
print(f'\n{alarms_by_severity_hour}')

print('\n------------------------------------------------------------------------------------')

#Identificar los tipos de alarmas mas comunes (basados en la columna TEXT).
tipos_comunes = datos['TEXT'].value_counts().head(10)
print(f"Tipos de Alarmas Más Comunes: {tipos_comunes}")
#Comparar la distribucion de tipos de alarmas en relacion con la severidad.
severidad_tipo = datos.groupby(['TEXT', 'SEVERITY']).size().unstack(fill_value=0)
print(f"\nDistribución de Tipos de Alarmas en Relación con la Severidad: {severidad_tipo}")

print('\n------------------------------------------------------------------------------------')

#Calcular cuantas alarmas se generan en cada subsistema o DN Red.
alarm_count = datos.groupby('DN')['ALARM_NUMBER'].count().reset_index(name='ALARM_COUNT')
alarm_names = datos.groupby(['DN', 'NAME']).size().reset_index(name='COUNT')
#Relacionar los nombres de alarmas (columna NAME) con los subsistemas que generan mas alarmas.
result = alarm_names.merge(alarm_count, on='DN')
print(f"Número de alarmas por subsistema: {alarm_count}")
print(f"\nRelación de nombres de alarmas con subsistemas: {result}")

print('\n------------------------------------------------------------------------------------')

#Grafico 1
#Mostrar la distribucion de alarmas por severidad.
severidad_counts = datos['SEVERITY'].value_counts()
severidad_counts.plot(kind='bar', color='skyblue')
plt.title('Distribución de Alarmas por Severidad')
plt.xlabel('Severidad')
plt.ylabel('Número de Alarmas')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
#Mostrar la frecuencia de los tipos de alarmas segun el texto descriptivo de la columna TEXT.
texto_counts = datos['TEXT'].value_counts().head(10)
texto_counts.plot(kind='bar', color='lightgreen')
plt.title('Frecuencia de Tipos de Alarmas')
plt.xlabel('Tipo de Alarma')
plt.ylabel('Número de Alarmas')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

print('\n------------------------------------------------------------------------------------')

#Gráfico 2
#Evolucion de la cantidad de alarmas a lo largo del dia o semana.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['Fecha'] = datos['ALARM_TIME'].dt.date
#Duracion promedio de las alarmas en funcion de la severidad.
alarm_count = datos.groupby('Fecha').size()
alarm_count.plot(kind='line')
plt.xlabel('Día de la semana')
plt.ylabel('Duración promedio de las alarmas')
plt.title('Duración promedio de las alarmas a lo largo de la semana')
plt.show()

print('\n------------------------------------------------------------------------------------')

#Grafico 3 
#Visualizar la proporcion de alarmas por severidad.
severidad_counts = datos['SEVERITY'].value_counts()
plt.pie(severidad_counts, labels=severidad_counts.index, autopct='%1.1f%%')
plt.title('Proporción de Alarmas por Severidad')
plt.show()
#Representar la proporcion de tipos de alarmas mas comunes en el sistema.
cinna = datos.groupby('DN')['SEVERITY'].count().sort_values(ascending=False).head(5)
plt.pie(cinna.values, labels=cinna.index, autopct='%1.1f%%')
plt.title('Proporción de Alarmas por Severidad')
plt.show()

print('\n------------------------------------------------------------------------------------')

#Grafico 4
#Relacion entre la duracion de las alarmas y su severidad.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['CANCEL_TIME'] = pd.to_datetime(datos['CANCEL_TIME'])
datos['DURATION'] = (datos['CANCEL_TIME'] - datos['ALARM_TIME']).dt.total_seconds() / 60
plt.scatter(datos['DURATION'], datos['SEVERITY'], alpha=0.5)
plt.title('Relación entre la duración de las alarmas y su severidad')
plt.xlabel('Duración (minutos)')
plt.ylabel('Severidad')
plt.grid(True)
plt.show()

print('\n------------------------------------------------------------------------------------')

#Grafico 5
#Distribucion de la severidad de las alarmas.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['CANCEL_TIME'] = pd.to_datetime(datos['CANCEL_TIME'])
datos['DURATION'] = (datos['CANCEL_TIME'] - datos['ALARM_TIME']).dt.total_seconds() / 60
severidad_counts = datos['SEVERITY'].value_counts()
severidad_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de la Severidad de las Alarmas')
plt.xlabel('Severidad')
plt.ylabel('Cantidad de Alarmas')
plt.xticks(rotation=0)
plt.grid(axis='y') 
plt.show()
#Distribucion de la duracion de las alarmas para observar si hay tiempos mas comunes en que las alarmas permaneces activas.
plt.hist(datos['DURATION'].dropna(), bins=30, color='salmon', edgecolor='black')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()

print('\n------------------------------------------------------------------------------------')































