import random
from typing import List, Optional
from app.config import lorem_settings

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