# Imagen base: Python 3.11 slim para mejor rendimiento y menor tamaño
FROM python:3.11-slim

# Añadir metadatos como buenas prácticas
LABEL maintainer="Lorem Ipsum API Team" \
      version="0.1.0" \
      description="API para generar texto Lorem Ipsum personalizable"

# Puerto configurable como argumento de construcción
ARG PORT=8000

# Establecer directorio de trabajo
WORKDIR /app

# Establecer variables de entorno generales
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    API_PORT=$PORT

# Variables para entorno de producción
ENV API_RELOAD=False \
    DEBUG=False \
    ENVIRONMENT=production

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Crear usuario no privilegiado para seguridad
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app

# Cambiar al usuario no privilegiado
USER appuser

# Exponer puerto configurable
EXPOSE $PORT

# Comando para ejecutar la aplicación con uvicorn directamente
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${API_PORT}"]