# Lorem Ipsum API

API REST desarrollada con FastAPI para generar texto Lorem Ipsum personalizable.

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)

## Características

- ✅ Generación de texto Lorem Ipsum personalizable
- ✅ Control sobre el número de párrafos
- ✅ Control sobre la longitud de los párrafos (min/max palabras)
- ✅ Opción para iniciar con la frase clásica "Lorem ipsum dolor sit amet"
- ✅ Documentación interactiva con Swagger UI y ReDoc
- ✅ Endpoints RESTful para integración sencilla

## Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/): Framework web moderno y de alto rendimiento
- [Uvicorn](https://www.uvicorn.org/): Servidor ASGI de alto rendimiento
- [Pydantic](https://docs.pydantic.dev/): Validación de datos y configuración

## Instalación y Uso

### Requisitos previos

- Python 3.11+

### Instalación local

1. Clonar el repositorio:
   ```
   git clone <url-del-repositorio>
   cd lorem-impsum-api
   ```

2. Crear y activar entorno virtual:
   ```
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```
   python -m app.main
   ```

La API estará disponible en http://localhost:8000 con documentación en http://localhost:8000/docs

### Configuración de entornos

La aplicación soporta diferentes entornos mediante variables de entorno o un archivo `.env` en la raíz del proyecto:

#### Variables de entorno principales

| Variable | Descripción | Valor por defecto |
|----------|-------------|------------------|
| API_HOST | Host para el servidor | "0.0.0.0" |
| API_PORT | Puerto para el servidor | 8000 |
| API_RELOAD | Habilitar recarga automática | true |
| DEBUG | Modo de depuración | false |
| ENVIRONMENT | Entorno (local/production) | "local" |
| CORS_ORIGINS_STR | Orígenes permitidos para CORS (JSON) | ["http://localhost:3000","http://localhost:8000"] |

#### Configuración para entorno local (desarrollo)

Crea un archivo `.env` en la raíz del proyecto:

```ini
# Configuración para desarrollo local
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true
DEBUG=true
ENVIRONMENT=local
CORS_ORIGINS_STR=["http://localhost:3000","http://localhost:8000"]
```

#### Configuración para entorno de producción

Para configurar el entorno de producción, puedes crear un archivo `.env` con estos valores:

```ini
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=false
DEBUG=false
ENVIRONMENT=production
CORS_ORIGINS_STR=["https://tudominio.com"]
```

O establecer estas variables de entorno directamente en tu sistema o servicio de hosting.

## API Endpoints

- **GET /api/v1/lorem/generate**: Genera texto Lorem Ipsum con parámetros de consulta
  - Parámetros: `paragraphs`, `min_words`, `max_words`, `start_with_lorem`

- **POST /api/v1/lorem/generate**: Genera texto Lorem Ipsum mediante JSON
  - Body: `{"paragraphs": 3, "min_words": 5, "max_words": 20, "start_with_lorem": true}`

- **GET /health**: Verificación de estado de la API

- **GET /docs**: Documentación interactiva (Swagger UI)

- **GET /redoc**: Documentación alternativa (ReDoc)

## Ejemplo de uso

### Petición GET
```
GET /api/v1/lorem/generate?paragraphs=2&min_words=5&max_words=10&start_with_lorem=true
```

### Petición POST
```json
POST /api/v1/lorem/generate
Content-Type: application/json

{
  "paragraphs": 2,
  "min_words": 5,
  "max_words": 10,
  "start_with_lorem": true
}
```

### Respuesta
```json
{
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi curabitur tempus.\n\nMaecenas feugiat consequat. Duis aute irure dolor voluptate velit esse.",
  "paragraphs": 2,
  "total_words": 20
}
```

## Desarrollo

1. Clonar el repositorio
2. Instalar dependencias de desarrollo
3. Crear una rama para tu característica
4. Enviar un Pull Request

## Licencia

Este proyecto está licenciado bajo la licencia MIT - ver el archivo LICENSE para más detalles.

## Autor

Jaolmos - https://github.com/Jaolmos

---

*Esta API es parte de mi portafolio de proyectos de desarrollo web.*
