print('\n------------------------------------------------------------------------------------\n')

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
d1 = pd.read_csv('Home/Archivos/AlarmasSistema.csv', sep=';') 
datos = pd.DataFrame(d1) 
print(datos)

print('\n------------------------------------------------------------------------------------')

#Calcular la cantidad de alarmas generadas para cada nivel de de severidad.
severidad_counts = datos['SEVERITY'].value_counts() #La funciona .vale_counts() va a leer la columna SEVERITY y la guardara en la variable severidad_count los juntara por severidad.
print(f'\nContador de severidad por nivel: {severidad_counts}') #Printeara todos los datos almacenados en severidad_counts segun la severidad 1,2,3,4.

print('\n------------------------------------------------------------------------------------')

#Identificar la severidad mas frecuente.
severidad_mas_frecuente = severidad_counts.idxmax() #La funcion .mode() buscara la severidad q tiene mas frecuencia en este caso seria la numero 2.
print(f'\nSeveridad mas frecuente: {severidad_mas_frecuente}') #Printeara el caso de severidad mas frecuente.

print('\n------------------------------------------------------------------------------------')

#Promedio y desviacion estandar de la severidad de alarmas
promedio_severidad = datos['SEVERITY'].mean()#Lo q hace la funcion .mean() es buscar el promedio de todos los datos dados por la columna severidad.
desviacion_estandar_severidad = datos['SEVERITY'].std()  #La funcion .std() calculara la desviacion estandar de todos los datos dados por la columna severidad.
print(f'\nPromedio: {promedio_severidad}')  #Printeara el promedio de la columna severidad.
print(f'\nDesviacion estandar: {desviacion_estandar_severidad}') #Printeara la desviacion estandar de la columna severidad.

print('\n------------------------------------------------------------------------------------')

#Obtener el Top 5 de los elementos que mas alarmas tienen segun severidad
top_5_elementos = datos['NAME'].value_counts().head(5) #creamos una variable la cual le asignamos el nombre de top_5_elementos y a la cual le asignaremos el analisis de los primeros 5 datos de la columna NAME.
print(f'Top 5 elementos: {top_5_elementos}') #Printearemos los primeros 5 elementos de la columna NAME.

print('\n------------------------------------------------------------------------------------')

#Calcular la duración promedio de las alarmas (diferencia entre la hora de inicio y la hora de cancelación).
datos['DURATION'] = pd.to_datetime(datos['CANCEL_TIME']) - pd.to_datetime(datos['ALARM_TIME']) #Lo q hace la funcion pd.to_datetime es analizar las filas de CANCEL_TIME Y ALARM_TIME y las restara para sacar una nueva columna llamada DURACION.
promedio_duracion = datos['DURATION'].mean() #Y de esa columna sacara el promedio de las alarmas.
print(f'\nPromedio duracion: {promedio_duracion}') #Y despues simplemente printeara el promedio.

print('\n------------------------------------------------------------------------------------')

#Identificar las alarmas con mayor y menor duración.
alarma_mayor = datos.loc[datos['DURATION'].idxmax()] #Lo q hara esta variable es buscar en la variable DURATION creada anteriormente el mayor dato en este caso la alarma_mayor.
alarma_menor = datos.loc[datos['DURATION'].idxmin()] #Lo q hara este variable es buscar en la variable DURATION creada anteriormente el menor dato en este caso la alarma_menor.
print(f'Alarma mayor: {alarma_mayor}\n') #Printeara la alarma_mayor.
print(f'Alarma menor: {alarma_menor}') #Printeara la alarma_menor.

print('\n------------------------------------------------------------------------------------')

print(f'\n{datos.groupby("SEVERITY")["DURATION"]}') #Relacionar la duracion de las alarmas con la severidad.

print('\n------------------------------------------------------------------------------------')

datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME']) #Aqui la variable datos['ALARM_TIME'] guarda los datos de esta misma pero pasara de str a fecha 

# Crear columnas adicionales
datos['hour'] = datos['ALARM_TIME'].dt.hour # La primera convertira los datos de ALARM_TIME como un dato hora con la funcion .dt.hour.
datos['day_of_week'] = datos['ALARM_TIME'].dt.day_name() # La segunda convertira los datos de ALARM_TIME como un dato de semana con la funcion .dt.day_name.
datos['month'] = datos['ALARM_TIME'].dt.month # La tercena convertira los datos de ALARM_TIME como un dato de mes con la funcion .dt.month.

# Análisis por hora
alarms_by_hour = datos.groupby('hour').size() #Esta variable agrupara los datos por la columna recien creada hour y contara el tamaño de esta y los juntara por valor.
print(f'\n{alarms_by_hour}') #Para despues printear esta como una cantidad de datos agrupados.

# Análisis por día de la semana
alarms_by_day = datos.groupby('day_of_week').size() #Esta variable agrupara los datos por la columna day_of_week y contara el tamaño de esta y los juntara por valor.
print(f'\n{alarms_by_day}') #Despues printeara esta como una cantidad de datos.

# Análisis por mes
alarms_by_month = datos.groupby('month').size() #Esta variable analizara las alarmas mensuales agrupando todos de la columna name y contado el tamaño de cada una.
print(f'\n{alarms_by_month}') #Printeara la variable como una cantidad de datos

# Comparar por severidad
alarms_by_severity_hour= datos.groupby(['hour', 'SEVERITY']).size().unstack().fillna(0) #Esta variable agrupara los valores de hour y Severidad y contara su tañano la funcion unstrack convertira el DataFrame de formato largo a ancho y el fillna(0) lo q hara es reemplazar datos nulos con 0.
print(f'\n{alarms_by_severity_hour}')#Printeara los datos como una cantidad de datos. 

print('\n------------------------------------------------------------------------------------')

# 1. Identificar los tipos de alarmas más comunes
tipos_comunes = datos['TEXT'].value_counts().head(10) # Esta variable se analiza lo datos mas comunes en la columna TXT haciendo un conteo de datos y seleccionando los primeros 10.
print(f"Tipos de Alarmas Más Comunes: {tipos_comunes}") #Printeara los 10 tipos de alarmas mas comunes. 

# 2. Comparar la distribución de tipos de alarmas en relación con la severidad
severidad_tipo = datos.groupby(['TEXT', 'SEVERITY']).size().unstack(fill_value=0) #la variable severidad_tipo hicimos una agrupacion entre la columna TEXT y SEVERITT donde analizamos el tamaño de cada una y ademas convertimos el data frame de una tamaño largo a ancho ademas de hacer q los valores nulos se hicieran cero con fill_value=0
print(f"\nDistribución de Tipos de Alarmas en Relación con la Severidad: {severidad_tipo}") #printeamos la variable 

print('\n------------------------------------------------------------------------------------')

# Agrupar por DN y contar las alarmas
alarm_count = datos.groupby('DN')['ALARM_NUMBER'].count().reset_index(name='ALARM_COUNT') #Agrupamos las comlumna DN y ALARM_NUMBER despues de eso se seleccionara la columna ALARM_NUMBER para trabajar sobre ella despues la funcion hara un conteo y por ultimo el .reset_index restablecera el indice del resultado asignadole un nuevo nombre el cual es ALARM_COUNT.

# Agrupar por DN y NAME para relacionar nombres de alarmas con subsistemas
alarm_names = datos.groupby(['DN', 'NAME']).size().reset_index(name='COUNT') #Agrupamos las columnas DN y NAME despues calculara el tamaño de esta y al resultado de eso se le asignara una nueva columan llamada COUNT

# Unir ambos DataFrames para tener una vista completa
result = alarm_names.merge(alarm_count, on='DN') # utilizamos la variable anteriormente hecha para combinar dos dataframes q en este caso seria la union entre alarm_names y alarm_count y se realizara en la columna DN.

# Mostrar el resultado.
print(f"Número de alarmas por subsistema: {alarm_count}") #printeara el subsistema
print(f"\nRelación de nombres de alarmas con subsistemas: {result}") #printeara la relacion de nombres con los subsistemas. 

print('\n------------------------------------------------------------------------------------')

#Grafico 1
# Agrupar por severidad y contar.
severidad_counts = datos['SEVERITY'].value_counts() #A la variable severidad_counts se le hara un contador de datos de la columna SEVERITY.

# Graficar.
severidad_counts.plot(kind='bar', color='skyblue') #A la variable anteriormente dada se le hara un grafico de barra con un color skyblue
plt.title('Distribución de Alarmas por Severidad') #Este es el titulo q tendra.
plt.xlabel('Severidad') #Esta es el nombre q tendra el eje x.
plt.ylabel('Número de Alarmas') #Este es el nombre q tendra el eje y.
plt.xticks(rotation=45) #Lo q hace el xticks es rotas las etiquetas y lo q hace el rotation 45 es girarla en 45 grados.
plt.grid(axis='y') #Generara lineas en el eje Y.

# Mostrar el gráfico.
plt.tight_layout() #Ayuda a q los textos no se pongan uno sobreotro.
plt.show()

# Agrupar por texto y contar.
texto_counts = datos['TEXT'].value_counts().head(10)  # Contara los datos de la variable TEXT y limitara a las 10 alarmas más frecuentes

# Graficar.
texto_counts.plot(kind='bar', color='lightgreen') #Se hara un grafico de la variable anterior tambien de barras y color verde claro.
plt.title('Frecuencia de Tipos de Alarmas') #Este es el titulo.
plt.xlabel('Tipo de Alarma') #El nombre del eje X
plt.ylabel('Número de Alarmas') #El nombre del eje Y.
plt.xticks(rotation=45) #Girara las etiquetas en 45 grados.
plt.grid(axis='y') #Hara lineas solo en el eje Y.

# Mostrar el gráfico.
plt.tight_layout() #Ayudara a q no se sobreponga el texto.
plt.show() #Mostrara el grafico.

print('\n------------------------------------------------------------------------------------')

#Gráfico 2
# Evolución de la cantidad de alarmas a lo largo del día o semana.
# Duración promedio de las alarmas en función de la severidad.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME']) #Convetira los datos de la columna ALARM_TIME a fecha 
datos['Fecha'] = datos['ALARM_TIME'].dt.date #Lo q hace la funcion .dt.date es extraer solo las fechas entonces estraera solo las fechas de ALARM_TIME y las guardara en la variable ALARM_TIME.
alarm_count = datos.groupby('Fecha').size() #Creara una variable donde se guardara el tamaño de los datos agrupados de Fecha 
alarm_count.plot(kind='line') #Asigna q de la variable anterior se hara un grafico de lineas.
plt.xlabel('Día de la semana') #Nombre q llevara el eje x.
plt.ylabel('Duración promedio de las alarmas') #Nombre q llevara el eje y.
plt.title('Duración promedio de las alarmas a lo largo de la semana') #Titulo q llevara el grafico.
plt.show() #Mostrara el grafico.

print('\n------------------------------------------------------------------------------------')

#Grafico 3 
#Visualizar la proporción de alarmas por severidad.
severidad_counts = datos['SEVERITY'].value_counts() #Guardara en una variable los datos de la columna SEVERITY y contara el valores de los datos.  
plt.pie(severidad_counts, labels=severidad_counts.index, autopct='%1.1f%%') #Hace un plt.pie donde el primer datos es (los datos de la variable anterior (counts) y el otro son los datos de la variable anterior pero con (index) y los convierte los datos en porcentaje.
plt.title('Proporción de Alarmas por Severidad') #Printea un titulo q dice Proporción de Alarmas por Severidad
plt.show() #Printea el grafico

#Representar la proporción de tipos de alarmas más comunes en el sistema.
cinna = datos.groupby('DN')['SEVERITY'].count().sort_values(ascending=False).head(5) #Creamos una variable donde esta agrupara los datos de DN y SEVERITY para despues contar los datos despues los ordenara de mayor a menor y por ultimo elegira los primeros 5.
plt.pie(cinna.values, labels=cinna.index, autopct='%1.1f%%') #Hacemos un grafico de pastel donde los datos a utilizar seras los de variable anterior pero como datos(values) y como texto(index) y despues el hacemos el autopct para q los muestre como porcentaje.
plt.title('Proporción de Alarmas por Severidad') #Este es el titulo q llevara el grafico.
plt.show() #Mostrara el grafico

print('\n------------------------------------------------------------------------------------')

#Grafico 4
#Gráfico de Dispersión: Relación entre la duración de las alarmas y su severida.
datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME']) #Convertira la columna de ALARM_TIME en fechas y la guardara en esta misma.
datos['CANCEL_TIME'] = pd.to_datetime(datos['CANCEL_TIME']) #Convertira la columna de CANCEL_TIME en fechas y la guardara en esta misma.

# Calcular la duración de las alarmas en minutos.
datos['DURATION'] = (datos['CANCEL_TIME'] - datos['ALARM_TIME']).dt.total_seconds() / 60 #Se hara una nueva columna llamada DURATION donde se restara la columna CANCEL_TIME y ALARM_TIME y los convertiremos a segundo con la .de.total_seconds y lo dividiremos por 60. 

# Crear el gráfico de dispersión.
plt.scatter(datos['DURATION'], datos['SEVERITY'], alpha=0.5) #El pl.t scatter generara un grafico de dispercion con los datos de duracion y severidad.
plt.title('Relación entre la duración de las alarmas y su severidad') #Este sera el titulo del grafico.
plt.xlabel('Duración (minutos)') #Este sera el nombre del eje x.
plt.ylabel('Severidad')#Este sera el nombre del eje Y.
plt.grid(True) # Esto generara las lineas en el fondo del grafico.
plt.show() #Esto mostrara el grafico.


print('\n------------------------------------------------------------------------------------')

datos['ALARM_TIME'] = pd.to_datetime(datos['ALARM_TIME']) #Esta variable almacenara los datos de ALARM_TIME como fecha y los guardara en esta misma.
datos['CANCEL_TIME'] = pd.to_datetime(datos['CANCEL_TIME']) #Esta variable almacenara los datos de CANCEL_TIME como fecha y los guardara en esta misma.

# Calcular la duración de las alarmas en minutos.
datos['DURATION'] = (datos['CANCEL_TIME'] - datos['ALARM_TIME']).dt.total_seconds() / 60 # Esta variable realizara una resta entre CANCEL_TIME menos ALARM_TIME para luego convertir el resultado en segundos y luego dividirlos en 60 para convertirlos en minutos.

# 1. Histograma de la distribución de la severidad de las alarmas.
severidad_counts = datos['SEVERITY'].value_counts() #Esta variable contara todos los datos de la columna de SEVERITY.
severidad_counts.plot(kind='bar', color='skyblue', edgecolor='black') #Esta variable hara un grafico de barras.
plt.title('Distribución de la Severidad de las Alarmas') #Este colocara el titulo del grafico.
plt.xlabel('Severidad') #Nombre del eje X.
plt.ylabel('Cantidad de Alarmas') #Nombre del eje Y.
plt.xticks(rotation=0) #Esta funcion hara una rotacion en 0 grados.
plt.grid(axis='y') #Esta funcion hace una separacion del eje Y.
plt.show() #Esta funcion mostrara el grafico.

# 2. Histograma de la distribución de la duración de las alarmas
plt.hist(datos['DURATION'].dropna(), bins=30, color='salmon', edgecolor='black') #Esta funcion hara un histograma con los datos de DURATION  y con el .dropna eliminara los datos nulos.
plt.xlabel('Duración (minutos)') #Sera el nombre del eje X.
plt.ylabel('Frecuencia') #Sera el nombre del eje Y.
plt.grid(axis='y') #Esta funcion hace una separacion del eje Y.
plt.show() #Esta funcion mostrara el grafico.

print('\n------------------------------------------------------------------------------------')































