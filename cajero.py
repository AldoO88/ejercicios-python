'''
Programa que simula un cajero automático básico, permitiendo al usuario consultar su saldo y retirar dinero.
'''

saldo_cliente = 5000

print("--- Bienvenido al Cajero Automático ---")
print("Su saldo actual es: $", saldo_cliente)

try: # bloque para manejar posibles errores en la entrada de datos
    cantidad_retirar = int(input("Ingresa la cantidad que deseas retirar: $")) # solicitamos la cantidad a retirar
    if cantidad_retirar <= saldo_cliente: # verificamos si hay suficiente saldo
        if cantidad_retirar % 100 == 0: # verificamos si la cantidad es múltiplo de 100
            saldo_cliente = saldo_cliente - cantidad_retirar # actualizamos el saldo
            print("Reriro exitoso.") # mostramos un mensaje de éxito

            sobrante = cantidad_retirar # variable para calcular los billetes a entregar

            billetes_500 = int(sobrante / 500) # calculamos la cantidad de billetes de 500
            sobrante = sobrante % 500 # actualizamos el sobrante

            billetes_200 = int(sobrante / 200) # calculamos la cantidad de billetes de 200
            sobrante = sobrante % 200 # actualizamos el sobrante

            billetes_100 = int(sobrante / 100) # calculamos la cantidad de billetes de 100 
            sobrante = sobrante % 100 # actualizamos el sobrante

            print("Entregnando...") # mostramos un mensaje
            print("Billetes de 500: ", billetes_500) # mostramos la cantidad
            print("Billetes de 200: ", billetes_200) # mostramos la cantidad
            print("Billetes de 100: ", billetes_100) # mostramos la cantidad
            print("Su saldo restante es: $", saldo_cliente) # mostramos el saldo restante

        else: # si la cantidad no es múltiplo de 100
            print("Error: La cantidad a retirar debe ser un múltiplo de 100.") # mostramos un mensaje de error
    else: # si no hay suficiente saldo
        print("Fondos insuficientes para realizar el retiro.") # mostramos un mensaje
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido para la cantidad a retirar.") # manejamos el error si la entrada no es numérica

        