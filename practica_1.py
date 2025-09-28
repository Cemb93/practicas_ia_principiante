# * 1. Generar listas con mas de 3 elementos
# * 2. Hacer al menos dos extracciones de cada elemento
array_1 = ["987", 987, 98.7, 252, True]
# ? IDX =    0     1    2     3
# ! ELE =    1     2    3     4
# TODO: array[idx 2: idx 4-1 = idx 3]

# ? Accediendo a los elementos 3 - 4
print('1:', array_1[2:4])
# ? Accediendo a los elementos 1 - 2
print('2:', array_1[0:2])

array_2 = ["654", 654, 75.7, 343, False]
# ? Accediendo al elemento 3
print('3:', array_2[2:3])
# ? Accediendo a los elementos 3 en adelante
print('4:', array_2[2:])