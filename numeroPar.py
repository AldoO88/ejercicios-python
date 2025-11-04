'''
Crear un programa que pida al usuario un número entero y le dé un análisis completo sobre él, 
determinando si es positivo, negativo o cero, y además si es par o impar.
'''

try: # bloque para manejar posibles errores en la entrada de datos
    #Pedir al usuario el número y convertirlo a entero
    #utilizamos int() para convertir la entrada a un número entero
    numero = int(input("Ingrese un número entero: ")) 

    if numero > 0: # verificamos si el número es positivo
        print("El número es positivo.") # mostramos un mensaje
        if numero % 2 == 0: # verificamos si el número es par
            print("Ademas el número es par.") # mostramos un mensaje   
        else: # si el número no es par, entonces es impar
            print("Ademas el número es impar.") # mostramos un mensaje
    elif numero < 0: # verificamos si el número es negativo
        print("El número es negativo.") # mostramos un mensaje
        if numero % 2 == 0: # verificamos si el número es par
            print("Ademas el número es par.") # mostramos un mensaje   
        else: # si el número no es par, entonces es impar
            print("Ademas el número es impar.") # mostramos un mensaje
    else: # si el número no es ni positivo ni negativo, entonces es cero
        print("El número es cero.") # mostramos un mensaje
except ValueError:
    print("Error: Eso no es un número entero. Inténtalo de nuevo.") # manejamos el error si la entrada no es numérica