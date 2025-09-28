personal_data={
    "name": "Carlos",
    "last_name": "Martinez",
    "age": 32,
    "profession": "Student",
}

# MODIFICAR
personal_data["age"]=42
#AGREGAR
personal_data["City"]="Bogota"
#print("Datos personales:", personal_data)

# Diccionario tienda
price_real=55.5
data_store={
    "price": price_real,
    "price_real": f"${price_real} USD",
    "name_product": "celphone",
    "pais_origen": "China",
    "pais_destino": "EE.UU",
}
#print("Datos de la tienda:", data_store)

# MODFICAR
data_store["price"]=1000
#AGREGAR
data_store["country"]="Colombia"
print("Datos reales:", data_store)