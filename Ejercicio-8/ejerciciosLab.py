def imprimirDiezVeces():
    palabra = input("Ingrese una palabra: ")

    for i in range(10):
        print(palabra)

def añosCumplidos():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))

            if edad < 0:
                print("Eror. La edad debe ser mayor a 0.")
                continue

            break

        except ValueError:
            print("Error, ingrese una edad válida")

    for i in range(0, edad + 1):
        print(i)

def numerosImpares():
    while True:
        try:
            numero = int(input("Ingrese un número positivo: "))

            if numero < 0:
                print("El número debe ser positivo.")
                continue
                
            break

        except ValueError:
            print("Ingrese un número válido.")

    print(", ".join(str(i) for i in range(0, numero + 1) if i % 2 != 0))

def cuentaAtras():
    while True:
        try:
            numero = int(input("Ingrese un número positivo: "))

            if numero <= 0:
                print("El número debe ser mayor a 0.")
                continue

            break

        except ValueError:
            print("Ingrese un número válido.")

    print(", ".join(str(i) for i in range(numero, -1, -1)))

def capitalObtenido():
    while True:
        try:
            capitalInicial = float(input("Ingrese una cantidad a invertir: "))

            if capitalInicial <= 0:
                print("La cantidad a invertir debe ser mayor a 0.")
                continue

            break

        except ValueError:
            print("Ingrese una cantidad válida.")
    
    while True:
        try:
            interesAnual = float(input("Ingrese el interes anual: "))

            if interesAnual < 0:
                print("El interes anual debe ser 0 o mayor a 0.")
                continue

            break

        except ValueError:
            print("Ingrese un interes anual válido.")
        
    while True:
        try:
            añosInversion = int(input("Ingrese el número de años a invertir: "))

            if  añosInversion < 0:
                print("La cantidad de años invertir debe ser 0 o mayor a 0.")
                continue

            break

        except ValueError:
            print("Ingrese una cantidad de años a invertir válida.")

    for i in range(1, añosInversion + 1):
        capitalObtenido = capitalInicial * (1 + interesAnual / 100)**i
        print(f"Año {i}: {capitalObtenido:.2f}")

def trianguloRectangulo():
    while True:
        try:
            altura = int(input("Ingrese la altura: "))

            if altura <= 0:
                print("La altura debe ser mayor a 0.")
                continue
            
            break

        except ValueError():
            print("Ingrese una altura válida.")
    
    for i in range(0, altura + 1):
        print("*" * i)

def tablaUnoDiez():
    for i in range(0, 11):
        print()
        print(f"Tabla de multiplicar del {i}")
        for j in range(0, 11):
            print(f"{i} x {j} = {i*j}")

def trianguloImpares():
    while True:
        try:
            altura = int(input("Ingrese un número: "))

            if altura <= 0:
                print("La altura debe ser mayor a 0.")
                continue

            break
        
        except ValueError:
            print("Ingrese una altura válida.")

    for i in range(1, altura + 1):
        for j in range(2*i -1, 0, -2):
            print(j, end=" ")
        print()

def contraseñaCorrecta():
    contraseña = "python123"

    while True:
        entrada = input("Ingrese la contraseña: ")

        if entrada != contraseña:
            print("Contraseña incorrecta.")
            continue

        if entrada == contraseña:
            print("Contraseña correcta.")
            break

def numeroPrimo():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            break

        except ValueError:
            print("Ingrese un número válido.")

    esPrimo = True

    if numero <= 1:
        esPrimo = False
    else:
        for i in range(2, int(numero / 2) + 1):
            if numero % i == 0:
                esPrimo = False
    
    if esPrimo:
        print("Es primo.")
    else:
        print("No es primo.")

def palabraInversa():
    palabra = input("Ingrese una palabra: ")

    for letra in palabra[::-1]:
        print(letra)

