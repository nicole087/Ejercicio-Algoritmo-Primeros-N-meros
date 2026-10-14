"Nombre: suma_n_primeros_numros"
"Entrada:n "
"Salida: suma"
"suma=0"
"contador=1"
"mientras contador <= n"
"contador= contador+1"
"Devolver suma"
def suma_n_numeros(n):
    suma = 0
    contador = 1
    while contador <= n:
        suma = suma + contador
        contador = contador + 1
    return suma

print(suma_n_numeros(3))
print(suma_n_numeros(5))