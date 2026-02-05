## Crear un entorno virtual en Python (Visual Studio / VS Code)

Un entorno virtual permite aislar las dependencias de tu proyecto y evitar conflictos con otros proyectos. Para crearlo, abre la terminal en la carpeta de tu proyecto y ejecuta:

```bash
python -m venv venv
```

Actívalo según tu sistema operativo: en Windows PowerShell venv\Scripts\Activate, en Windows CMD venv\Scripts\activate.bat y en macOS/Linux source venv/bin/activate. Luego, selecciona el intérprete en Visual Studio / VS Code con Ctrl + Shift + P → Python: Select Interpreter → venv.

Dentro del entorno virtual puedes instalar paquetes. Por ejemplo, para instalar numpy:

```bash
pip install numpy
```
