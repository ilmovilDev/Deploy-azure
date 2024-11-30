# Proyecto de Prueba - Despliegue en Azure 🌐

Este es un proyecto de prueba diseñado para aprender y experimentar con el despliegue de aplicaciones utilizando **Azure App Services** y contenedores Docker. 🚀

## 🛠️ Tecnologías utilizadas

- **🐍 Python 3.11**: Lenguaje principal.
- **🌐 Flask**: Framework para desarrollar la API.
- **🐳 Docker**: Contenedores para fácil implementación.

## 🚀 Instalación y configuración

### 1. Clonar el repositorio y acceder al directorio del proyecto
```bash
git clone https://github.com/ilmovilDev/repositorio.git
cd repositorio
```

## 🐍 Configuración del entorno virtual

### 1. Crear el entorno virtual
```bash
py -3.11 -m venv nombre_del_entorno
```

### 2. Activar el entorno virtual
Windows
```bash
nombre_del_entorno\Scripts\activate
```

Linux/MacOS
```bash
source nombre_del_entorno/bin/activate
```

### 3. Desactivar el entorno virtual
```bash
deactivate
```

## 📦 Instalación de dependencias y pruebas del endpoint

### 1. Instalar las dependencias

Con el entorno virtual activado, instala los paquetes necesarios:
```bash
pip install -r requirements.txt
```

### 2. Ejecutar el proyecto en local
Inicia la aplicación Flask:
```bash
python main.py
```

Si todo funciona correctamente, deberías ver algo como esto:
* Running on http://127.0.0.1:5000

## 🐳 Uso de Docker

### 1. Construir la imagen del contenedor
```bash
docker build -t nombre_de_la_imagen .
```

### 2. Ejecutar el contenedor
```bash
docker run -p 5000:5000 nombre-de-la-imagen
```
La aplicación estará disponible en: http://localhost:5000

## 🌐 Despliegue en Azure

