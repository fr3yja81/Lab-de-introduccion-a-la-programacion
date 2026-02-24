print("Loggin")

intentos = 0

while True:
    user = input("Usuario: ")
    password = input("Contraseña: ")

    digitosPassword = len(password)

    if user == "":
        print("El usuario no puede estar vacio.")
        continue

    if password == "":
        print("La contraseña no puede estar vacia.")
        continue

    elif chr(32) in password:
        print("La contraseña no debe contener espacios.")
        continue

    elif digitosPassword < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue


    if not password.isdigit():
        print("La contraseña debe contener al menos un número.")
    elif not password.isalpha():
        print("La contraseña debe contener al menos una letra.")

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