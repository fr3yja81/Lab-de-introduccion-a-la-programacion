# Explicación del sistema de login --- paso a paso

## Mensaje inicial

``` python
print("Loggin")
```

Muestra en pantalla que el sistema de login ha iniciado.

------------------------------------------------------------------------

## Contador de intentos

``` python
intentos = 0
```

Guarda el número de intentos fallidos. Sirve para bloquear el acceso
después de 3 errores.

------------------------------------------------------------------------

## Bucle principal

``` python
while True:
```

Crea un ciclo infinito que mantiene el programa ejecutándose hasta:

-   acceso correcto\
-   bloqueo por intentos

------------------------------------------------------------------------

## Entrada de datos

``` python
user = input("Usuario: ")
password = input("Contraseña: ")
```

Solicita al usuario sus credenciales.

------------------------------------------------------------------------

## Longitud de la contraseña

``` python
digitosPassword = len(password)
```

Cuenta los caracteres de la contraseña para validar su tamaño.

------------------------------------------------------------------------

## Validación de usuario vacío

Si el usuario no escribe nada:

-   se muestra un mensaje de error\
-   el ciclo reinicia con `continue`

------------------------------------------------------------------------

## Validaciones de contraseña

Se revisa que:

-   no esté vacía\
-   no tenga espacios\
-   tenga al menos 8 caracteres

Si falla alguna condición, el ciclo se reinicia.

------------------------------------------------------------------------

## Verificación de letra y número

``` python
for letra in password:
```

Se recorre la contraseña para confirmar que contenga:

-   al menos una letra\
-   al menos un número

Si no cumple, se reinicia el ciclo.

------------------------------------------------------------------------

## Validación de acceso

``` python
if user == "admin" and password == "admin2026":
```

Si las credenciales coinciden:

-   acceso concedido\
-   el programa termina

Si no:

-   se suma un intento\
-   se muestra el contador

------------------------------------------------------------------------

## Bloqueo del sistema

Si hay 3 intentos fallidos:

-   el acceso se bloquea\
-   el ciclo termina

------------------------------------------------------------------------

## Resumen

El programa:

-   valida entradas\
-   evita contraseñas débiles\
-   controla intentos\
-   concede o bloquea acceso

Es un ejemplo educativo de control básico de autenticación.
