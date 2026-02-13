# Conversor de Decimal a Binario, Hexadecimal, Octal y Booleano

## ¿Qué hace el programa?

Este programa pide un número decimal y lo convierte a:

- Binario  
- Hexadecimal  
- Octal  
- Booleano  

---

## Cómo funciona la conversión

Para binario, octal y hexadecimal usamos la misma idea:

1. Dividir el número entre la base (2, 8 o 16).
2. Guardar el residuo usando `%`.
3. Dividir usando `//` (división entera).
4. Repetir hasta que el número llegue a 0.
5. Escribir los residuos al revés.

En hexadecimal, cuando el residuo es mayor que 9, usamos letras:

- A = 10  
- B = 11  
- C = 12  
- D = 13  
- E = 14  
- F = 15  

---

## Comandos importantes que usamos

### `def`
Sirve para crear funciones.  
Nos ayuda a dividir el programa en partes más organizadas.

### `return`
Devuelve el resultado de la función.

### `while`
Repite el código mientras la condición sea verdadera.  
Lo usamos para seguir dividiendo hasta llegar a 0.

### `if / elif / else`
Sirve para tomar decisiones dependiendo de una condición.

### `//`
División entera (sin decimales).

### `%`
Obtiene el residuo de una división.  
Es lo más importante para hacer las conversiones.

### `bool()`
Convierte un número en `True` o `False`.

- 0 → False  
- Cualquier otro número → True  

### `try / except`
Evita que el programa se rompa si el usuario escribe algo que no es número.

### `break`
Sirve para salir del ciclo del menú.

---

## En resumen

Este programa combina:

- Funciones  
- Ciclos  
- Condicionales  

Y todo se basa en dividir y guardar residuos para cambiar de base numérica.