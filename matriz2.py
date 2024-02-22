matriz = [[1,3,5],
          [7,9,11],
          [13,15,17]
          ]
valor_buscado = 13

if any(valor_buscado in fila for fila in matriz):
    print(f"se encontro(valor_buscado) en la matriz.")
else:
    print(f"(valor encontrado) no se encontro en la matriz.")
