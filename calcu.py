import math
import os

def Menu():

    print("1.- Suma        2.- Resta       3.-Multiplicación       4.- División")
    print("")
    print("5.- Potencia    6.- Raíz Cudrada        7.- Seno          8.- Coseno")
    print("")
    print("9.- Tangente    10.- Borr. Pant.        11.- Menú         12.- Salir ")
    print("")


def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        mcd = b
        b = a % b
        a = mcd
    return mcd


def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm


def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def Calculadora():
    Menu()

    opc = int(input("Selecione nº de Opción: "))

    while (opc > 0 and opc < 24):

        if (opc == 1):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print('La Suma es:', num1 + num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 1

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 1

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))


        elif (opc == 2):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print('La Resta es:', num1 - num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 2

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 2

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

        elif (opc == 3):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print('La Multiplicacion es:', num1 * num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 3

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 3

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

        elif (opc == 4):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")

            try:
                print('La Division es:', num1 / num2)
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 4

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")

                    if Continuar == "s" or Continuar == "S":
                        opc = 4

                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))

            except ZeroDivisionError:
                print('No se Permite la Division Entre 0')
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 4

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")

                    if Continuar == "s" or Continuar == "S":
                        opc = 4

                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))


        elif (opc == 5):
            print("")
            base = int(input("Ingrese Base: "))
            print("")
            exponente = int(input("Ingrese Exponente: "))
            print("")
            print('La Potencia es:', base ** exponente)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 5

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 5

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

        elif (opc == 6):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("La raíz cuadrada de {} es {}".format(num, math.sqrt(num)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 6

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 6

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))

        elif (opc == 7):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El seno de {} es {}".format(radianes, math.sin(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 7

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:

                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 7

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))



        elif (opc == 8):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El coseno de {} es {}".format(radianes, math.cos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 8

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 8

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))


        elif (opc == 9):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La tangente de {} es {}".format(radianes, math.tan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 9

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))

            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 9

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))




        elif (opc == 10):
            borrarPantalla()
            Menu()
            opc = int(input("Selecione nº de Opción: "))

        elif (opc == 11):
            Menu()
            opc = int(input("Selecione nº de Opción: "))

        elif (opc == 12):
            exit(0)

    while (opc < 1 or opc > 13):
        print("")
        print("Opción no Encontrada")
        print("")
        opc = int(input("Selecione nº de Opción: "))


Calculadora()
