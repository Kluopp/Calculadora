"""
-----------------------------------------------------------------------------------------------
Título: Calculadora
Fecha: 16/09/2024
Autor: Pablo Bellagamba

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("No se puede dividir por cero.")
        return None
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        return None
    return numero ** 0.5

def solicitar_opcion():
    opcion = int(input("Seleccione una opción (0-6): "))
    if 0 <= opcion <= 6:
        return opcion
    else:
        print("Por favor, elija una opción válida.")
        mostrar_menu()
        return solicitar_opcion()

def mostrar_menu():
    print("--- Calculadora Avanzada ---")
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicación")
    print("4 División")
    print("5 Potencia")
    print("6 Raíz Cuadrada")
    print("0 Salir")



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():

    while True:
        mostrar_menu()
        opcion = solicitar_opcion()

        if opcion == 0:
            print("Gracias.")
            break

        elif 1 <= opcion <= 4:  
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if opcion == 1:
                print(f"Resultado: {suma(a, b)}")
            elif opcion == 2:
                print(f"Resultado: {resta(a, b)}")
            elif opcion == 3:
                print(f"Resultado: {multiplicacion(a, b)}")
            elif opcion == 4:
                resultado = division(a, b)
                if resultado is not None:
                    print(f"Resultado: {resultado}")

        elif opcion == 5:  
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print(f"Resultado: {potencia(base, exponente)}")

        elif opcion == 6:  
            numero = float(input("Ingrese el número: "))
            resultado = raiz_cuadrada(numero)
            if resultado is not None:
                print(f"Resultado: {resultado}")


# Punto de entrada al programa
main()
