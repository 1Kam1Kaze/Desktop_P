print('\n------------------------------------------------------------------------------------\n')

#Librerias utilizadas 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lectura del archivo 
d1 = pd.read_csv('Home/Archivos/AlarmasSistema.csv', sep=';')
datos = pd.DataFrame(d1)
print(datos)

print('\n------------------------------------------------------------------------------------')

#Calcular la cantidad de alarmas generadas por cada nivel de severidad 
severidad_counts = datos['SEVERITY'].value_counts()
print(f'\nContador de severidad por nivel: {severidad_counts}')

print('\n------------------------------------------------------------------------------------')

#Identificar severidad mas frecuente
severidad_mas_frecuente = severidad_counts.idxmax()
print(f'\nSeveridad mas frecuente: {severidad_mas_frecuente}')

print('\n------------------------------------------------------------------------------------')

promedio_severidad = datos['SEVERITY'].mean()
desviacion_estandar_severidad = datos['SEVERITY'].std()
print(f'\nPromedio: {promedio_severidad}')
print(f'\nDesviacion estandar: {desviacion_estandar_severidad}')

print('\n------------------------------------------------------------------------------------')

top_5_elementos = datos['NAME'].value_counts().head(5)
print(f'Top 5 elementos: {top_5_elementos}')

print('\n------------------------------------------------------------------------------------')

datos['DURATION'] = pd.to_datetime(datos['CANCEL_TIME']) - pd.to_datetime(datos['ALARM_TIME'])
promedio_duracion = datos['DURATION'].mean()
print(f'\nPromedio duracion: {promedio_duracion}')

print('\n------------------------------------------------------------------------------------')

alarma_mayor = datos.loc[datos['DURATION'].idxmax()]
alarma_menor = datos.loc[datos['DURATION'].idxmin()]
print(f'Alarma mayor: {alarma_mayor}\n')
print(f'Alarma menor: {alarma_menor}')

print('\n------------------------------------------------------------------------------------')

print(f'\n{datos.groupby("SEVERITY")["DURATION"]}')

print('\n------------------------------------------------------------------------------------')

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
alarms_by_severity_hour= datos.groupby(['hour', 'SEVERITY']).size().unstack().fillna(0)
print(f'\n{alarms_by_severity_hour}')

print('\n------------------------------------------------------------------------------------')

tipos_comunes = datos['TEXT'].value_counts().head(10)
print(f"Tipos de Alarmas Más Comunes: {tipos_comunes}")
severidad_tipo = datos.groupby(['TEXT', 'SEVERITY']).size().unstack(fill_value=0)
print(f"\nDistribución de Tipos de Alarmas en Relación con la Severidad: {severidad_tipo}")

print('\n------------------------------------------------------------------------------------')

alarm_count = datos.groupby('DN')['ALARM_NUMBER'].count().reset_index(name='ALARM_COUNT')
alarm_names = datos.groupby(['DN', 'NAME']).size().reset_index(name='COUNT')
result = alarm_names.merge(alarm_count, on='DN')
print(f"Número de alarmas por subsistema: {alarm_count}")
print(f"\nRelación de nombres de alarmas con subsistemas: {result}")

print('\n------------------------------------------------------------------------------------')

#Grafico 1
severidad_counts = datos['SEVERITY'].value_counts()
severidad_counts.plot(kind='bar', color='skyblue')
plt.title('Distribución de Alarmas por Severidad')
plt.xlabel('Severidad')
plt.ylabel('Número de Alarmas')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
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
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['Fecha'] = datos['ALARM_TIME'].dt.date
alarm_count = datos.groupby('Fecha').size()
alarm_count.plot(kind='line')
plt.xlabel('Día de la semana')
plt.ylabel('Duración promedio de las alarmas')
plt.title('Duración promedio de las alarmas a lo largo de la semana')
plt.show()

print('\n------------------------------------------------------------------------------------')

#Grafico 3 
severidad_counts = datos['SEVERITY'].value_counts()
plt.pie(severidad_counts, labels=severidad_counts.index, autopct='%1.1f%%')
plt.title('Proporción de Alarmas por Severidad')
plt.show()
cinna = datos.groupby('DN')['SEVERITY'].count().sort_values(ascending=False).head(5)
plt.pie(cinna.values, labels=cinna.index, autopct='%1.1f%%')
plt.title('Proporción de Alarmas por Severidad')
plt.show()

print('\n------------------------------------------------------------------------------------')

#Grafico 4
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
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME'])
datos['CANCEL_TIME'] = pd.to_datetime(datos['CANCEL_TIME'])
datos['DURATION'] = (datos['CANCEL_TIME'] - datos['ALARM_TIME']).dt.total_seconds() / 60
severidad_counts = datos['SEVERITY'].value_counts()
severidad_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de la Severidad de las Alarmas')
plt.xlabel('Severidad')
plt.ylabel('Cantidad de Alarmas')
plt.xticks(rotation=0)
plt.grid(axis='y') plt.show()
plt.hist(datos['DURATION'].dropna(), bins=30, color='salmon', edgecolor='black')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()

print('\n------------------------------------------------------------------------------------')































