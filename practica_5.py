import pandas as pd
#* SE INSTALO "openpyxl" PARA LA LECTURA EN EXCEL

# !NOTA: INSTALAR LA EXTENCION "Better Comments" PARA VISUALIZAR MEJOR LOS COMENTARIOS 
# TODO: 1. Cargar el fichero de excel 'dataset_bigdata' y nombrarlo 'df_practica5'
ruta_bd = r'C:\Users\USUARIO\Desktop\PROGRAMACION\Artificial Inteligent\Nivel Basico\Base de datos'
nombre_del_archivo = '\dataset_bigdata.xlsx'
df_practica5 = pd.read_excel(f'{ruta_bd}{nombre_del_archivo}')
print(f'---------- PRIMER PUNTO ----------\n{df_practica5}\n\n')

# TODO: 2. Analizar solo eventos batch de redes con tamano_gb >=6
condicion = (
    (df_practica5['origen_datos'] == 'redes') &
    (df_practica5['tamano_gb'] >= 6) &
    (df_practica5['tipo_procesamiento'] == 'batch')
)
filtrando_eventos = df_practica5[condicion]
print(f'---------- SEGUNDO PUNTO ----------\n{filtrando_eventos}\n\n')

# TODO: 3. Imputar los NaN con la mediana de las columnas 'latencia_ms' y 'etiqueta_anomalia' (separados)
mediana_lms = df_practica5['latencia_ms'].median(skipna=True)
mediana_etan = df_practica5['etiqueta_anomalia'].median(skipna=True)
df_practica5_imp = df_practica5.copy()
df_practica5_imp['latencia_ms'] = df_practica5_imp['latencia_ms'].fillna(mediana_lms) # * REEMPLAZO LOS VALORES NULL
df_practica5_imp['etiqueta_anomalia'] = df_practica5_imp['etiqueta_anomalia'].fillna(mediana_etan) # * REEMPLAZO LOS VALORES NULL
print(f'---------- TERCER PUNTO ----------\n{df_practica5_imp}\n\n')

"""
    TODO: 4. Con los nuevos valores de las columnas del punto 3 agrupar por tipo de procesamiento y calcular:
    * Cantidad de registros
    ? Media de 'tamano_gb'
    * total de eventos por seg
"""
df_agrupado = df_practica5_imp.groupby('tipo_procesamiento').agg(
    registros=('id_registro','count'), # * HAY 4 DE "batch" Y 4 DE "stream"
    promedio_tgb=('tamano_gb','mean'),
    total_even=('tasa_eventos_por_seg','sum')
).reset_index()
print(f'---------- CURATO PUNTO ----------\n{df_agrupado}\n')