# Lorem Ipsum API

API REST desarrollada con FastAPI para generar texto Lorem Ipsum personalizable.

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)

## Características

- ✅ Generación de texto Lorem Ipsum personalizable
- ✅ Control sobre el número de párrafos
- ✅ Control sobre la longitud de los párrafos (min/max palabras)
- ✅ Opción para iniciar con la frase clásica "Lorem ipsum dolor sit amet"
- ✅ Documentación interactiva con Swagger UI y ReDoc
- ✅ Completamente dockerizado
- ✅ Endpoints RESTful para integración sencilla

## Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/): Framework web moderno y de alto rendimiento
- [Uvicorn](https://www.uvicorn.org/): Servidor ASGI de alto rendimiento
- [Pydantic](https://docs.pydantic.dev/): Validación de datos y configuración
- [Docker](https://www.docker.com/): Contenedorización para despliegue sencillo

## Instalación y Uso

### Requisitos previos

- Python 3.11+
- Docker (opcional, para despliegue con contenedores)

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

En producción, especialmente al usar Docker, las variables se configuran automáticamente con valores seguros:

```ini
API_RELOAD=false
DEBUG=false
ENVIRONMENT=production
```

Puedes sobrescribir estas variables al ejecutar el contenedor Docker:

```bash
docker run -d -p 8000:8000 \
  -e API_PORT=8000 \
  -e DEBUG=false \
  -e ENVIRONMENT=production \
  -e CORS_ORIGINS_STR='["https://tudominio.com"]' \
  --name lorem-api lorem-ipsum-api:latest
```

### Despliegue con Docker

#### Construcción de la imagen:
```
# Construir la imagen
docker build -t lorem-ipsum-api:latest .

# Reconstruir sin caché (útil si hay problemas)
docker build --no-cache -t lorem-ipsum-api:latest .
```

#### Ejecución del contenedor:
```
# Ejecutar en primer plano (ver logs directamente)
docker run -p 8000:8000 --name lorem-api lorem-ipsum-api:latest

# Ejecutar en segundo plano
docker run -d -p 8000:8000 --name lorem-api lorem-ipsum-api:latest

# Ejecutar en segundo plano con reinicio automático
docker run -d --restart always -p 8000:8000 --name lorem-api lorem-ipsum-api:latest
```

#### Gestión del contenedor:
```
# Detener el contenedor
docker stop lorem-api

# Iniciar el contenedor si está detenido
docker start lorem-api

# Reiniciar el contenedor
docker restart lorem-api

# Eliminar el contenedor (debe estar detenido)
docker rm lorem-api
```

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

[Tu nombre] - [Tu sitio web/GitHub]

---

*Esta API es parte de mi portafolio de proyectos de desarrollo web.*
