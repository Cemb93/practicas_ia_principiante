integer=input("Escribre un numero: ")
number_int=0
if integer >= "0":
    number_int=int(integer)
# number_int=int(input("Escribre un numero: "))

number_float=float(integer)
if integer >= "0.0":
    number_float=int(integer)
# number_float=float(input("Escribre un numero: "))

if number_int >= 0:
    print("Es integer")
elif number_float >= 0.0:
    print("Es flotante")
else:
    print("Es negativo")
    