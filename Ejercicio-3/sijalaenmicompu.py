print("Inicia sesión")

intentos = 0
acceso = 0

while intentos < 3:

    user = input("Usuario: ")
    password = input("Contraseña: ")

    if user == "":
        print("El usuario no puede estar vacío.")
        intentos += 1

    elif password == "":
        print("La contraseña no puede estar vacía.")
        intentos += 1

    elif " " in password:
        print("La contraseña no debe contener espacios.")
        intentos += 1

    elif len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        intentos += 1

    elif not any(c.isdigit() for c in password):
        print("La contraseña debe contener al menos un número.")
        intentos += 1

    elif not any(c.isalpha() for c in password):
        print("La contraseña debe contener al menos una letra.")
        intentos += 1

    elif user == "admin" and password == "admin2026":
        print("Acceso concedido")
        acceso = 1
    
    else:
        print("Acceso denegado")
        intentos += 1

    print(f"Intentos: {intentos}")

    if intentos >= 3:
        print("Demasiados intentos. Acceso bloqueado.")
        break

    while acceso == 1:
            print("1. Clasificar número.")
            print("2. Categoria de edad y permisos.")
            print("3. Calcular tarifa final.")
            print("4. Cerrar sesión.")
            print("5. Final")
            opcion = int(input("Seleccione una de la opciones anteriores: "))

            if opcion == 1:
                print("Clasificar número.")
            
            elif opcion == 2:
                print("Categoria de edad y perimsos.")
            
            elif opcion == 3:
                print("Calcular tarifa final.")

            elif opcion == 4:
                print("Sesión cerrada.")
                acceso = 0

            elif opcion == 5:
                acceso = -1
                break

            else: 
                print("Error, opción inválida.")

    if acceso == -1:
        print("Programa Finalizado.")
        break
