#Calculareos el 15 % de las siguientes compras en descuento
def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_con_descuento = precio - descuento
    return precio_con_descuento



# Ejemplo de uso:
precio_original = int(input("Ingrese precio:"))
porcentaje_descuento = int(input("porcentaje:"))
precio_con_descuento = calcular_descuento(precio_original, porcentaje_descuento)
print("Precio final: $", precio_original)
print("Porcentaje de descuento:", porcentaje_descuento, "%")
print("Precio con descuento: $", precio_con_descuento)

6
def calcular_iva(subtotal, porcentaje_iva = 12):
    valor_iva = (subtotal * porcentaje_iva) / 100
    return valor_iva

monto_subtotal = 100
monto_iva = calcular_iva(monto_subtotal)
monto_total = monto_subtotal + monto_iva
print(f'Monto Total: {monto_total}')


monto_subtotal = 100
porcentaje_iva = 5
monto_iva = calcular_iva(monto_subtotal, porcentaje_iva)
monto_total = monto_subtotal + monto_iva
print(f'Monto Total: {monto_total}')