informacion_personal={'Nombre':'Ramiro','Edad':'34','Telefono':'0962791900','Ciudad':'Quito'}

informacion_personal['Profesion'] = 'Electricista'
print(informacion_personal)
informacion_personal['Ciudad'] = 'Guayaquil'
print(informacion_personal)
informacion_personal['Estado Civil'] = 'Casado'
print(informacion_personal)
del informacion_personal['Edad']
print(informacion_personal)
# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Quito'
informacion_personal['provincia'] = 'Pichincha'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Docente'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0987654321'








