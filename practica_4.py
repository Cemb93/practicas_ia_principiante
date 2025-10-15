import pandas as pd

# !NOTA: INSTALAR LA EXTENCION "Better Comments" PARA VISUALIZAR MEJOR LOS COMENTARIOS 
# TODO: 1. Cargar el archivo 'estudiantes_ejercicio.csv' y comprobar que las columnas nuevas existen
ruta_archivo = r"C:\Users\USUARIO\Desktop\PROGRAMACION\Artificial Inteligent\Nivel Basico\Base de datos"
nombre_del_archivo = 'copy_estudiantes_original.csv'
df = pd.read_csv(f'{ruta_archivo}\{nombre_del_archivo}', index_col=0)

df['Aprobado'] = df["Promedio_10"] >= 8.0
df['Promedio_100'] = df['Promedio_10'] * 10
# print('========== PRIMER PUNTO ==========')
# print(f'1 - MANIPULACION DE DATOS:\n{df}\n\n')

# TODO: 2. Calcular la media, mediana y la moda de la columna 'Promedio 10'
# print('========== SEGUNDO PUNTO ==========')
# print(
#   f'CALCULANDO LA MEDIA DE (PROMEDIO_10): {df["Promedio_10"].mean()}\n\n'
#   f'CALCULANDO LA MEDIANA DE (PROMEDIO_10): {df["Promedio_10"].median()}\n\n'
#   f'CALCULANDO LA MODA DE (PROMEDIO_10): \n{df["Promedio_10"].mode().to_string(index=False)}\n\n'
# )

# TODO: 3. Filtrar los estudiantes con 'Aprobado' == True y obtener la lista de nombres
aprobados = df[df["Aprobado"] == True]
estudiantes_aprobados = aprobados["Nombre"].tolist()
# print('========== TERCER PUNTO ==========')
# print(f'LOS ESTUDIANDO APROBADOS SON:\n{estudiantes_aprobados}\n\n')

# TODO: 4. Encontrar la carrera con mayor promedio medio
# * SE AGRUPA SOLO LA COLUMNA "Carrera"
# ? SE GENERA UNA COLUMNA LLAMADA "top_carrera" LA CUAL TIENE EL PROMEDIO
agr = df.groupby("Carrera").agg(top_carrera=("Promedio_10", "max"))
carrera_mayor_promedio = agr.sort_values("top_carrera", ascending=False).head(1)
# print('========== CUARTO PUNTO ==========')
# print(f'CARRERA CON MAYOR PROMEDIO: \n{carrera_mayor_promedio}\n\n')

# TODO: 5. Crear una columna nueva 'Diferencia' = Promedio_100 - (Edad * 2) y explicar el resultado. 
# print('========== QUINTO PUNTO ==========')
df["Diferencia"] = df["Promedio_100"] - df["Edad"] * 2
# print(f'CREANDO COLUMNA DIFERENCIA: \n{df}\n\n')

# TODO: 6. Guardar un subconjunto (Nombre, Carrera, Promedio_10, Aprobado) en un nuevo archivo CSV. 
subset = df[["Nombre", "Carrera", "Promedio_10", "Aprobado"]]
# print('========== SEXTO PUNTO ==========')
# print(subset)

ruta_archivo_3 = f'{ruta_archivo}\practica4_estudiantes_original.csv'
subset.to_csv(ruta_archivo_3)
practica_4 = pd.read_csv(ruta_archivo_3, index_col=0)
print(f'RESULTADO FINAL: \n{practica_4}')