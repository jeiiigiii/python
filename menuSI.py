
import os

def euro_dolares(divisa, tasa):
    dolares = divisa / tasa
    print("El cambio de euro a dolar es:", dolares)

def dolares_euro(divisa, tasa):
    euros = divisa * tasa
    print("El cambio de dolar a euro es:",euros)

def euro_yen(divisa, tasa):
    yen = divisa / tasa
    print("El cambio de euro a yen es:", yen)

def recorrer_directorio(ruta):
    for file in os.listdir(ruta):
        file_path = os.path.join(ruta, file)
        print(file_path)
        if os.path.isdir(file_path):
            print("Es un directorio:", file_path)
        else:
            print("Es un archivo:", file_path)

def menu():
    print("1-Ingresar cantidad")
    print("2-Cambio de divisa Euro/dolar")
    print("3-Cambio de divisa Dolar/Euro")
    print("4-Cambio de divisa Euro/YEN")
    print("5-Recorrer ruta y Comparador")
    print("6-Salir")

def ingresar_divisa():
    divisa = float(input("Ingrese un numero: "))
    return divisa


def ingresar_ruta():
    ruta = input("Ingresa tu ruta: ")
    return ruta

print("Bienvenido a la calculadora de cambio de divisa y otras vainas")
opcion = ""

while opcion != "6":
    os.system('sleep 3')
    os.system('clear')
    menu()
    opcion = input("Ingrese su opción (1-6): ")

    if opcion == "1":
        divisa=ingresar_divisa()
        
    elif opcion == "2":
        tasa=1.18
        euro_dolares(divisa,tasa)
    elif opcion == "3":
        tasa=0.90
        dolares_euro(divisa, tasa)
    elif opcion == "4":
       tasa=2
       euro_yen(divisa, tasa)
    elif opcion == "5":
        ruta = ingresar_ruta()
        recorrer_directorio(ruta)
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente de nuevo.")
