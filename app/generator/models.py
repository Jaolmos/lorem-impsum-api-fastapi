import random
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from app.config import lorem_settings

# Modelos para la API
class LoremIpsumRequest(BaseModel):
    """
    Modelo para las solicitudes de generación de Lorem Ipsum
    """
    paragraphs: int = Field(1, ge=1, le=lorem_settings.MAX_PARAGRAPHS, 
                          description="Número de párrafos a generar")
    min_words: int = Field(5, ge=1, description="Mínimo de palabras por párrafo")
    max_words: int = Field(20, ge=5, le=lorem_settings.MAX_WORDS_PER_PARAGRAPH, 
                         description="Máximo de palabras por párrafo")
    start_with_lorem: bool = Field(True, description="Si debe comenzar con 'Lorem ipsum dolor sit amet'")
    
    def validate_word_range(self):
        """
        Valida que el rango de palabras sea correcto
        
        Raises:
            ValueError: Si min_words > max_words
        """
        if self.min_words > self.max_words:
            raise ValueError(f"El mínimo de palabras ({self.min_words}) no puede ser mayor que el máximo ({self.max_words})")
        return True
    
    @validator('paragraphs')
    def validate_paragraphs(cls, v):
        if v > lorem_settings.MAX_PARAGRAPHS:
            raise ValueError(f"El número máximo de párrafos permitido es {lorem_settings.MAX_PARAGRAPHS}")
        return v
    
    @validator('max_words')
    def validate_max_words(cls, v):
        if v > lorem_settings.MAX_WORDS_PER_PARAGRAPH:
            raise ValueError(f"El número máximo de palabras por párrafo permitido es {lorem_settings.MAX_WORDS_PER_PARAGRAPH}")
        return v

class LoremIpsumResponse(BaseModel):
    """
    Modelo para las respuestas de generación de Lorem Ipsum
    """
    text: str = Field(..., description="Texto Lorem Ipsum generado")
    paragraphs: int = Field(..., description="Número de párrafos generados")
    total_words: int = Field(..., description="Número total de palabras generadas")

class ErrorResponse(BaseModel):
    """
    Modelo para respuestas de error
    """
    detail: str = Field(..., description="Descripción del error")

# Generador de Lorem Ipsum
class LoremIpsumGenerator:
    """
    Generador de texto Lorem Ipsum con opciones de personalización
    """
    
    def __init__(self):
        """
        Inicializa el generador con palabras base de Lorem Ipsum
        """
        self.words = lorem_settings.BASE_WORDS
    
    def get_random_words(self, count: int) -> List[str]:
        """
        Obtiene un número específico de palabras aleatorias
        
        Args:
            count: Número de palabras a generar
            
        Returns:
            Lista de palabras aleatorias
        """
        return [random.choice(self.words) for _ in range(count)]
    
    def generate_paragraph(self, 
                          min_words: int = 5, 
                          max_words: int = 20,
                          start_with_lorem: bool = True) -> str:
        """
        Genera un párrafo de texto Lorem Ipsum
        
        Args:
            min_words: Mínimo de palabras en el párrafo
            max_words: Máximo de palabras en el párrafo
            start_with_lorem: Si debe comenzar con "Lorem ipsum dolor sit amet"
            
        Returns:
            Párrafo generado
        """
        # Verificar límites de palabras
        if min_words < 1:
            min_words = 1
        
        if max_words > lorem_settings.MAX_WORDS_PER_PARAGRAPH:
            max_words = lorem_settings.MAX_WORDS_PER_PARAGRAPH
            
        if min_words > max_words:
            min_words = max_words
        
        # Determinar la cantidad de palabras para este párrafo
        word_count = random.randint(min_words, max_words)
        
        # Generar el párrafo
        if start_with_lorem and word_count >= 5:
            # Comenzar con el clásico "Lorem ipsum dolor sit amet"
            paragraph_words = ["Lorem", "ipsum", "dolor", "sit", "amet"]
            
            # Agregar palabras adicionales si es necesario
            if word_count > 5:
                paragraph_words.extend(self.get_random_words(word_count - 5))
        else:
            # Generar párrafo con palabras aleatorias
            paragraph_words = self.get_random_words(word_count)
        
        # Asegurar que la primera palabra comience con mayúscula
        paragraph_words[0] = paragraph_words[0].capitalize()
        
        # Agregar un punto al final
        paragraph = " ".join(paragraph_words) + "."
        return paragraph
    
    def generate_text(self, 
                     paragraphs: int = 1, 
                     min_words: int = 5, 
                     max_words: int = 20,
                     start_with_lorem: bool = True) -> str:
        """
        Genera texto Lorem Ipsum con múltiples párrafos
        
        Args:
            paragraphs: Número de párrafos a generar
            min_words: Mínimo de palabras por párrafo
            max_words: Máximo de palabras por párrafo
            start_with_lorem: Si el primer párrafo debe comenzar con "Lorem ipsum dolor sit amet"
            
        Returns:
            Texto completo con los párrafos generados
        """
        # Verificar límite de párrafos
        if paragraphs > lorem_settings.MAX_PARAGRAPHS:
            paragraphs = lorem_settings.MAX_PARAGRAPHS
        
        if paragraphs < 1:
            paragraphs = 1
        
        # Generar párrafos
        result = []
        for i in range(paragraphs):
            # Solo el primer párrafo comienza con Lorem ipsum si se especifica
            should_start_with_lorem = start_with_lorem and (i == 0)
            paragraph = self.generate_paragraph(
                min_words=min_words,
                max_words=max_words,
                start_with_lorem=should_start_with_lorem
            )
            result.append(paragraph)
        
        # Unir párrafos con saltos de línea
        return "\n\n".join(result)

# Instancia global del generador
lorem_generator = LoremIpsumGenerator()