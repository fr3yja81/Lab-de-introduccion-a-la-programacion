#conversor
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    negativo = numero < 0
    numero = abs(numero)
    resultado = ""
    
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero //= 2
    
    if negativo:
        resultado = "-" + resultado
        
    return resultado


def decimal_a_hexadecimal(numero):
    if numero == 0:
        return "0"
    
    digitos = "0123456789ABCDEF"
    negativo = numero < 0
    numero = abs(numero)
    resultado = ""
    
    while numero > 0:
        resultado = digitos[numero % 16] + resultado
        numero //= 16
    
    if negativo:
        resultado = "-" + resultado
        
    return resultado


def decimal_a_octal(numero):
    if numero == 0:
        return "0"
    
    negativo = numero < 0
    numero = abs(numero)
    resultado = ""
    
    while numero > 0:
        resultado = str(numero % 8) + resultado
        numero //= 8
    
    if negativo:
        resultado = "-" + resultado
        
    return resultado


def decimal_a_booleano(numero):
    return bool(numero)


def menu():
    while True:
        print("\nCONVERSOR DE NÚMEROS")
        print("1. Decimal a Binario")
        print("2. Decimal a Hexadecimal")
        print("3. Decimal a Octal")
        print("4. Decimal a Booleano")
        print("5. Convertir a TODO")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "6":
            print("Programa finalizado.")
            break
        
        if opcion in ["1", "2", "3", "4", "5"]:
            try:
                numero = int(input("Ingrese un número decimal: "))
                
                if opcion == "1":
                    print("Binario:", decimal_a_binario(numero))
                
                elif opcion == "2":
                    print("Hexadecimal:", decimal_a_hexadecimal(numero))
                
                elif opcion == "3":
                    print("Octal:", decimal_a_octal(numero))
                
                elif opcion == "4":
                    print("Booleano:", decimal_a_booleano(numero))
                
                elif opcion == "5":
                    print("\n--- RESULTADOS COMPLETOS ---")
                    print("Binario:", decimal_a_binario(numero))
                    print("Hexadecimal:", decimal_a_hexadecimal(numero))
                    print("Octal:", decimal_a_octal(numero))
                    print("Booleano:", decimal_a_booleano(numero))
            
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")
        
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()