#Autor David Yair Fernández salas
# Matricula A01747088
# Este programa realiza varias acciones corresponidentes a la tarea

"""Esta función realiza la operación de divisón y toma los parametros que el usuario introduce(dividendo y el divisor
y al final regresa el mensaje de quien es el divisor, el dividendo y cual es el resultado de la operación"""
def dividir(Dividendo,Divisor):
    cociente=0
    residuo= Dividendo

    while Divisor<= residuo:
        residuo= residuo-Divisor
        cociente+=1
    print(Dividendo,"/",Divisor,"=",cociente,"sobra",residuo)


"""Esta función como el nombre lo dice encuentra el valor entre n números, los parametros que usa son introducidos por 
el usuario, y esta función compara cual es el mayor con la función de if y elif, y al final devuelve un mensaje 
donde dice cual es le valor más grande"""
def encontrarMayor():
    valorAtras= -1
    valorActual= 0
    contador= 0

    print("Teclea una serie de números para encontrar el mayor.")
    while valorActual!= -1:
        valorActual=int(float(input("Teclea un número [-1 para salir]:")))

    if valorActual<-1:
        print("No hay valor mayor")
    elif valorActual>valorAtras:
        valorAtras=valorActual
        contador+=1
    elif valorActual< -1:
        print("Ese no es un valor válido: Debes teclear un número entero positivo.")

    elif valorActual == -1:
        if contador != 0:
            print("El mayor es: ",valorAtras)
        else:
            print("No hay valor mayor")


"""Esta fución es la principal y aqui es donde el usario puede ver el menu que tiene este programa y dependiendo 
de la opción que tome, la función mandará los parametros especiales para cada función que necesite estos valores """
def main():
    opcion = 0
    while opcion != 3:
        if opcion == 0:
            print("Misión 07. Ciclos while")
            print("Autor: David Yair Fernández Salas")
            print("Matrícula: A01747088")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))

        elif opcion == 1:
            print("Calculando divisiones")
            Dividendo = abs(int(float(input("Dividendo: "))))
            Divisor= abs(int(float(input("Divisor: "))))
            dividir(Dividendo,Divisor)

            opcion = 0
            print("")

        elif opcion == 2:
            encontrarMayor()
            opcion= 0
        elif opcion == 3:
            print("")
            print("Gracias por ejecutar el programa, regresa pronto")
            break
        elif opcion < 0 or opcion > 3:
                print("ERROR, teclea 1, 2 o 3")
                opcion = 0

"Se llama a la función main para correr el programa."
main()