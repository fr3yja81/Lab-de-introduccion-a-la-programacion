print("Loggin")

intentos = 0

while True:
    user = input("Usuario: ")

    password = input("Contraseña: ")

    digitosPassword = len(password)

    if user == "":
         print("El usuario no puede estar vacio.")

    elif user == "":
         print("El usuario no puede estar vacio.")

    
    if password == "":
         print("La contraseña no puede estar vacia.")

    elif chr(32) in password:
            print("La contraseña no debe contener espacios.")
            break
    

    elif digitosPassword < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue

    for letra in password:
        if letra.isdigit():
            print("La contraseña debe contener al menos una letra.")
            break

        elif letra.isalpha():
            print("La contraseña debe contener al menos un número.")
            break

        else:
             continue

    if user == "admin" and password == "admin2026":
        print("Acceso concedido")
        break

    else:
        print("Acceso denegado")
        intentos += 1
        print(f"Intentos: {intentos}")

        if intentos >= 3:
            print("Demasiados intentos. Acceso bloqueado.")
            break