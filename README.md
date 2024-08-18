# API REST de Gestión de Cursos con FastAPI

Este proyecto es una API REST sencilla para gestionar cursos, creada utilizando FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una "base de datos" simulada, que se almacena en memoria.

## Contenido

- [Requisitos](#requisitos)
- [Librerías Utilizadas](#librerías-utilizadas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejecutar la API](#ejecutar-la-api)
- [Probar la API](#probar-la-api)
- [Rutas de la API](#rutas-de-la-api)
- [Documentación de la API](#documentación-de-la-api)
- [Ejemplos de Cursos](#ejemplos-de-cursos)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Requisitos

Para ejecutar este proyecto necesitarás tener instalados:

- **Python 3.7+**
- **pip** (para instalar dependencias)

## Librerías Utilizadas

### 1. **FastAPI**
   - **Descripción**: FastAPI es un framework moderno y de alto rendimiento para construir APIs con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.
   - **Propósito**: Es el framework principal utilizado para definir las rutas, manejar las solicitudes HTTP y generar automáticamente la documentación interactiva de la API.
   - **Instalación**:
     ```bash
     pip install fastapi
     ```

### 2. **Uvicorn**
   - **Descripción**: Uvicorn es un servidor ASGI de alto rendimiento que se usa para ejecutar aplicaciones construidas con FastAPI.
   - **Propósito**: Uvicorn se utiliza para ejecutar la aplicación FastAPI en un entorno de producción o desarrollo. Permite que la API maneje solicitudes HTTP de manera eficiente.
   - **Instalación**:
     ```bash
     pip install uvicorn
     ```

### 3. **Pydantic**
   - **Descripción**: Pydantic es una librería que facilita la validación de datos y la creación de modelos de datos en Python utilizando anotaciones de tipo.
   - **Propósito**: Se utiliza para definir los modelos de datos (como `Curso`) y garantizar que las entradas de datos en la API cumplan con los requisitos especificados.
   - **Instalación**: Pydantic se instala automáticamente como una dependencia de FastAPI, por lo que no necesitas instalarla por separado.

### 4. **uuid**
   - **Descripción**: `uuid` es un módulo integrado en Python que proporciona herramientas para generar identificadores únicos universales (UUID).
   - **Propósito**: Se utiliza para generar identificadores únicos para cada curso creado en la API, asegurando que cada recurso tenga un `id` único.
   - **Instalación**: `uuid` es parte de la biblioteca estándar de Python, por lo que no requiere instalación adicional.

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/ea-analisisdatos/fastapi.git
cd fastapi