# Crear un entorno virtual en Python con VS Code (Windows)

Esta guía explica **de forma sencilla** cómo crear y usar un entorno virtual de Python en **Visual Studio Code** si usas **Windows**.

---

## ¿Qué es un entorno virtual y por qué usarlo?

Un entorno virtual es básicamente un **espacio aislado** para tu proyecto.

Sirve para:

* No mezclar librerías entre proyectos
* Evitar errores raros
* Tener todo más ordenado

En resumen: **usa entornos virtuales siempre**.

---

## Cosas que necesitas antes

Asegúrate de tener instalado:

* **Python 3**
* **Visual Studio Code**
* **Extensión de Python en VS Code** (la de Microsoft)

Para comprobar que Python está bien instalado, abre la terminal y escribe:

```bash
python --version
```

Si sale algo tipo `Python 3.x.x`, todo bien.

---

## 1. Crear la carpeta del proyecto

1. Crea una carpeta (por ejemplo: `mi_proyecto_python`)
2. Ábrela en **VS Code** (`Archivo → Abrir carpeta`)

---

## 2. Abrir la terminal en VS Code

Dentro de VS Code:

* Presiona **Ctrl + Ñ**
* Se abrirá una terminal abajo

Asegúrate de que estés dentro de la carpeta del proyecto.

---

## 3. Crear el entorno virtual

En la terminal escribe:

```bash
python -m venv venv
```

Esto crea una carpeta llamada `venv` donde vive el entorno virtual.

---

## 4. Activar el entorno virtual

### Si usas PowerShell (lo normal en VS Code):

```bash
venv\Scripts\Activate.ps1
```

### Si usas CMD:

```bash
venv\Scripts\activate
```

Si todo salió bien, verás algo así:

```text
(venv) C:\tu\proyecto>
```

Ese `(venv)` significa que **ya estás dentro del entorno virtual**.

---

## 5. Decirle a VS Code qué Python usar

Esto es importante para que VS Code no se confunda.

1. Presiona **Ctrl + Shift + P**
2. Escribe: `Python: Select Interpreter`
3. Elige el que diga algo como:

```text
venv\Scripts\python.exe
```

Listo, VS Code ya sabe qué Python usar 

---

## 6. Instalar librerías

Con el entorno activado, instala librerías, por ejemplo:

```bash
pip install numpy
```

Para ver lo que tienes instalado:

```bash
pip list
```

## Resumen

```bash
python -m venv venv
venv\Scripts\activate
pip install lo_que_necesites
```