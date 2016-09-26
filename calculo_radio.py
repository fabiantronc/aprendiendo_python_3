# Calculo radio
# Creo una variable con el valor de PI
pi = 3.14158
# Le pedimos datos al usuario
respuesta = raw_input('Cual es su radio ')
# Transformamos esos datos a valores flotantes
respuesta_validada = float(respuesta)
#Realizamos la operacion matematica
area = pi * respuesta_validada**2
print'El area es', area