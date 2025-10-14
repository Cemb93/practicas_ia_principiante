
# !NOTA: INSTALAR LA EXTENCION "Better Comments" PARA VISUALIZAR MEJOR LOS COMENTARIOS 
"""
    TODO: 1. HACER 3 DICCIONARIOS:
    * UNO SIMPLE ANIDADO
    ? UN DICCIONARIO DE DICCIONARIOS
    ! UNO CON LISTAS
"""

# * DICCIONARIO SIMPLE ANIDADO
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "direccion": {
        "ciudad": "Bogotá",
        "pais": "Colombia",
        "codigo_postal": 110111
    }
}

print('========== PRIMER PUNTO ==========')
print(f'Ciudad de: {persona["direccion"]["ciudad"]}')  # Salida: Bogotá

# MODIFICANDO PROPIEDAD
persona["direccion"]["pais"] = "México"

# AGREGANDO PROPIEDAD
persona["direccion"]["calle"] = "Calle 123"

print(f'Diccionario actualizado:\n{persona}')
print('\n')

# ? DICCIONARIO DE DICCIONARIOS
estudiantes = {
    "est1": {
        "nombre": "Ana",
        "edad": 20,
        "carrera": "Ingeniería"
    },
    "est2": {
        "nombre": "Luis",
        "edad": 22,
        "carrera": "Medicina"
    },
    "est3": {
        "nombre": "María",
        "edad": 19,
        "carrera": "Arquitectura"
    }
}

print(f'Carrera de: {estudiantes["est3"]["carrera"]}') # Salida: Arquitectura

# SE AGREGA UN NUEVO ESTUDIANTE
estudiantes["est4"] = {
    "nombre": "Carlos",
    "edad": 21,
    "carrera": "Derecho"
}

# Modificar un valor existente
estudiantes["est1"]["edad"] = 21
print(f'Diccionario 2 actualizado:\n{estudiantes}')
print('\n')

curso = {
    "nombre": "Inteligencia Artificial con Python",
    "instructor": "Juan Carlos Aguilar",
    "estudiantes": ["Ana", "Luis", "María", "Carlos"],
    "calificaciones": [4.5, 3.8, 4.9, 4.2]
}

print(f'Estudiante de IA: {curso["estudiantes"][2]}') # Salida: María

# Se agrega un nuevo estudiante y su calificación al final de la lista
curso["estudiantes"].append("Sofía")
curso["calificaciones"].append(4.7)
print(f'Diccionario 3 actualizado:\n{curso}')
print('\n')
print('========== SEGUNDO PUNTO ==========')

"""
    TODO: 2. HACER 4 CONJUNTOS
    * HACER 2 ELIMINACIONES
    ? HACER 2 ADICIONES
    ! REALIZAR 3 OPERACIONES ENTRE CONJUNTOS
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {7, 8, 9}
D = {1, 3, 5, 7, 9}

# ? ✔ ADICIONES
A.add(6)
C.add(10)
# ! 🔹 ELIMINACIONES
B.remove(4)
D.discard(9)

print("Después de adiciones y eliminaciones:")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}\n")

# * 💻 OPERACIONES ENTRE CONJUNTOS
union_AB = A | B # SE UNEN SIN REPETIR NUMEROS
interseccion_AD = A & D # SE UNEN SOLO LOS NUMEROS REPETIDO
union_AC = A.union(C)

print("Operaciones entre conjuntos:")
print(f"Unión entre A - B = {union_AB}")
print(f"Intersección entre A - D = {interseccion_AD}")
print(f"Union entre A - C = {union_AC}")
