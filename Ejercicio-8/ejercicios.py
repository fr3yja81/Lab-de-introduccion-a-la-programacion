def imprimirDiezVeces():
    palabra = input("Ingrese una palabra: ")

    for i in range(1, 11):
        print(f"{i}.- {palabra}")

def añosCumplidos():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Ingrese una edad válida")

        if edad < 0:
            print("Ingrese una edad válida.")
            continue

        for i in range(1, edad + 1):
            print(i)
            
def imparesEnteros():
        while True:
            try:
                numero = int(input("Ingrese un número: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

        impares = []

        for i in range(0, numero + 1):
            if i % 2 != 0:
                impares.append(str(i))

        print(", ".join(impares))

def cuentaAtras():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    if numero > 0:
        cuentaAtras = []

        for i in range(numero, -1, -1):
            cuentaAtras.append(str(i))
        
        print(", ".join(cuentaAtras))
    else:
        print("El número debe ser mayor a 0.")

def inversion():
    cantidad = float(input("Ingrese una cantidad a invertir: "))
    interes = float(input("Ingrese el interes anual: "))
    tiempo = int(input("Ingrese la cantidad de tiempo: "))

    for i in range(1, tiempo + 1):
        cantidad = cantidad * (1 + interes / 100)**tiempo 
        print(f"Año: {i} : {cantidad}")

def triangulo():
    altura = int(input("Ingrese la altura: "))

    for i in range(1, altura, 1):
        print("*" * i)
