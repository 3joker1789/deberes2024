print('Cuidad Quito:')
print('Temperatuas cada 7 dias')


temperaturas = [
    [18,20,23],
    [10,25,16],
    [17,]
]
suma = 0
for fila in temperaturas:
    for elemento in fila:
        suma += elemento
        print(elemento)

temperaturas = [
    [19,20,23],
    [14,25,16],
    [17,]
]
suma1 = 0

for fila in temperaturas:
    for elemento in fila:
        suma += elemento
        print(elemento)

print(f'La suma total: {suma+suma1}')

promedio = suma / len(temperaturas)
print(f' Promedio de filas es: {promedio}')
print(f'El promedio real es :{promedio/6}')

print('Cuidad Guayaquil:')
print('Temperatuas cada 7 dias')
temperaturas = [
    [24,26,28],
    [25,25,26],
    [21,]
]

suma = 0

for fila in temperaturas:
    for elemento in fila:
        suma += elemento
        print(elemento)
print(f'La suma total: {suma}')
promedio = suma / len(temperaturas)
print(f' Promedio de filas es: {promedio}')
print(f'El promedio real es :{promedio/3}')