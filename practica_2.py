name="Carlos"
age=32
year=2025
high=1.80
print(
  "Primer punto:", 
  f"\n✔ Nombre: {name} \n✔ Edad: {age} \n✔ Anio: {year} \n✔ Estatura: {high}"
)
print('=======================================')

numeros_enteros=(20, 25, 13)
numero_decimal=1.79
cadenas_de_texto=('Primer string', 'Segundo string')

array=[
  numeros_enteros,
  numero_decimal,
  cadenas_de_texto
]

value_1=f"🔴 Extrayento el entero: {array[0][2]}"
value_2=f"🔴 Extrayento el decimal: {array[1]}"
value_3=f"🔴 Extrayento el texto: {array[2][1]}"
print(f'Segundo Punto:\n{value_1}\n{value_2}\n{value_3}')