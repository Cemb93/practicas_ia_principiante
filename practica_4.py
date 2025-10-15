import pandas as pd
import os

# !NOTA: INSTALAR LA EXTENCION "Better Comments" PARA VISUALIZAR MEJOR LOS COMENTARIOS 
# TODO: 1. Cargar el archivo 'estudiantes_ejercicio.csv' y comprobar que las columnas nuevas existen
ruta_archivo = r"C:\Users\USUARIO\Desktop\PROGRAMACION\Artificial Inteligent\Nivel Basico\Base de datos"
nombre_del_archivo = 'copy_estudiantes_original.csv'
df = pd.read_csv(f'{ruta_archivo}\{nombre_del_archivo}')

# df['Aprobado'] = df["Promedio"] >= 8.0
df['Aprobado'] = df["Promedio_10"] >= 8.0
df['Promedio_100'] = df['Promedio_10'] * 10
df = df.rename(columns={"Promedio": "Promedio_10"})
print('========== PRIMER PUNTO ==========')
print('MANIPULACION DE DATOS:')
print(df)
print('\n')

# TODO: 2. Calcular la media, mediana y la moda de la columna 'Promedio 10'
print('========== SEGUNDO PUNTO ==========')
print(f'CALCULANDO LA MEDIA DE (PROMEDIO_10): {df["Promedio_10"].mean()}')
print('\n')
print(f'CALCULANDO LA MEDIANA DE (PROMEDIO_10): {df["Promedio_10"].median()}')
print('\n')
print(f'CALCULANDO LA MODA DE (PROMEDIO_10): \n{df["Promedio_10"].mode()}')
print('\n')

# TODO: 3. Filtrar los estudiantes con 'Aprobado' == True y obtener la lista de nombres
aprobados = df[df["Aprobado"] == True]
estudiantes_aprobados = aprobados["Nombre"].tolist()
print('========== TERCER PUNTO ==========')
print('LOS ESTUDIANDO APROBADOS SON:\n', estudiantes_aprobados)
print('\n')

# TODO: 4. Encontrar la carrera con mayor promedio medio
agr = df.groupby("Carrera").agg(max_carrera=("Promedio_10","max"))
carrera_mayor_promedio = agr.sort_values("max_carrera", ascending=False).head(1)
print('========== CUARTO PUNTO ==========')
print(carrera_mayor_promedio)

# 5. Crear una columna nueva 'Diferencia' = Promedio_100 - (Edad * 2) y explicar el resultado. 
# df["Diferencia"] = df["Promedio_100"] - df["Edad"] * 2
# print(df) 

# 6. Guardar un subconjunto (Nombre, Carrera, Promedio_10, Aprobado) en un nuevo archivo CSV. 
subset = df[["Nombre", "Carrera", "Promedio_10", "Aprobado"]]
print('========== SEXTO PUNTO ==========')
# print(subset)

ruta_archivo_3 = f'{ruta_archivo}\practica4_estudiantes_original.csv'
subset.to_csv(ruta_archivo_3)
practica_4 = pd.read_csv(ruta_archivo_3)
print(practica_4)