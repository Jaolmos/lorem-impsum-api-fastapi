import json
from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    """
    Configuración de la aplicación basada en variables de entorno
    
    Esta clase permite cargar configuración desde variables de entorno y archivo .env
    """
    # Configuración de la API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True
    
    # Entorno y Depuración
    DEBUG: bool = False
    ENVIRONMENT: str = "local"
    
    # Configuración CORS
    CORS_ORIGINS_STR: str = '["http://localhost:3000","http://localhost:8000"]'
    
    @property
    def CORS_ORIGINS(self) -> List[str]:
        """
        Convertir la cadena JSON a lista de orígenes permitidos para CORS
        """
        return json.loads(self.CORS_ORIGINS_STR)
    
    @property
    def is_production(self) -> bool:
        """
        Comprueba si la aplicación está en entorno de producción
        """
        return self.ENVIRONMENT.lower() == "production"
    
    class Config:
        """
        Configuración de Pydantic para cargar variables desde .env
        """
        env_file = ".env"  # Carga desde .env
        case_sensitive = True

# Crear instancia de configuración global
settings = Settings()

# Configuración específica del generador Lorem Ipsum
class LoremIpsumSettings:
    """
    Configuración para el generador de Lorem Ipsum
    """
    MAX_PARAGRAPHS: int = 10
    MAX_WORDS_PER_PARAGRAPH: int = 100
    DEFAULT_START_WITH_LOREM: bool = True
    # Palabras base para generación
    BASE_WORDS: List[str] = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", 
        "adipiscing", "elit", "sed", "do", "eiusmod", "tempor",
        "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"
    ]

lorem_settings = LoremIpsumSettings()