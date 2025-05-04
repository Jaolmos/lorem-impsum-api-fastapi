from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api.v1.endpoints import router as api_router
from app.config import settings

# Crear la aplicación FastAPI
app = FastAPI(
    title="Lorem Ipsum API",
    description="API para generar texto Lorem Ipsum personalizable",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas API v1
app.include_router(api_router, prefix="/api/v1")

# Ruta raíz
@app.get("/", include_in_schema=False)
async def root():
    """
    Redirecciona a la documentación de la API
    """
    return RedirectResponse(url="/docs")

# Ruta de verificación de estado
@app.get("/health", tags=["health"])
async def health_check():
    """
    Verifica que la API está funcionando correctamente
    """
    return {
        "status": "ok",
        "version": "0.1.0",
        "environment": settings.ENVIRONMENT
    }

# Ejecutar con uvicorn si se llama directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host=settings.API_HOST, 
        port=settings.API_PORT, 
        reload=settings.API_RELOAD
    )