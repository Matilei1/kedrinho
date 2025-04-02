# Guía de Instalación y Uso

Este archivo proporciona instrucciones para configurar el entorno de desarrollo y ejecutar el proyecto correctamente.

## Crear y activar el entorno virtual:

Primero, debes crear el entorno virtual y luego activarlo. Ejecuta los siguientes comandos:

```bash
python -m venv venv && venv\Scripts\activate && Set-ExecutionPolicy Unrestricted -Scope Process.

Este comando:

Crea el entorno virtual (python -m venv venv).

Activa el entorno virtual en Windows usando CMD o PowerShell (venv\Scripts\activate).

Permite la ejecución de scripts en PowerShell si es necesario (Set-ExecutionPolicy Unrestricted -Scope Process).

# Instalar Dependencias:
Una vez el entorno esté activado, instala todas las librerías necesarias utilizando pip. Ejecuta el siguiente comando para instalar las dependencias del proyecto y algunas librerías adicionales:

pip install -r requirements.txt && pip install pandas kedro-datasets kedro-viz

Una vez instaladas las librerias, puedes ejecutar kedro con el comando "kedro run" o visualizar las pipelines con el comando "kedro viz"
