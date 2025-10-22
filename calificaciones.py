'''
Programa que permite ingresar las calificaciones de los tres trimestres de un estudiante, 
calcule el promedio y muestre un mensaje dependiendo el promedio obtenido.
'''

promedio = 0.0 # declaramos la variable promedio para almacenar el promedio de las calificaciones

try: # bloque para manejar posibles errores en la entrada de datos
    calificacion1 = float(input("Ingrese la calificación del primer trimestre: ")) # solicitamos la calificación del primer trimestre
    calificacion2 = float(input("Ingrese la calificación del segundo trimestre: ")) # solicitamos la calificación del segundo trimestre
    calificacion3 = float(input("Ingrese la calificación del tercer trimestre: ")) # solicitamos la calificación del tercer trimestre
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3 # calculamos el promedio de las calificaciones

    if promedio >= 6.0 and promedio < 7.0: # verificamos si el promedio es mayor o igual a 6.0
        print("Tu promedio es: ", promedio, "¡Aprobaste!, Necesitas Mejorar") # mostramos un mensaje
    elif promedio >= 7.0 and promedio < 8.0: # verificamos si el promedio está entre 7.0 y 7.9
        print("Tu promedio es: ", promedio, "¡Aprobaste!, Puedes hacerlo mejor") # mostramos un mensaje
    elif promedio >= 8.0 and promedio < 9.0: # verificamos si el promedio está entre 8.0 y 8.9
        print("Tu promedio es: ", promedio, "¡Aprobaste!, Buen trabajo") # mostramos un mensaje
    elif promedio >= 9.0 and promedio <= 10.0: # verificamos si el promedio está entre 9.0 y 10.0
        print("Tu promedio es: ", promedio, "¡Aprobaste!, Excelente trabajo") # mostramos un mensaje
    else: # si el promedio es menor a 6.0
        print("Tu promedio es: ", promedio, "¡Reprobaste el año escolar!") # mostramos un mensaje
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido para las calificaciones.") # manejamos el error si la entrada no es numérica
