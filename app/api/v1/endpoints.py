from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.generator.models import LoremIpsumRequest, LoremIpsumResponse, ErrorResponse
from app.generator.lorem import lorem_generator

# Crear router para los endpoints de la versión 1
router = APIRouter(prefix="/lorem", tags=["lorem-ipsum"])

@router.post(
    "/generate", 
    response_model=LoremIpsumResponse,
    responses={400: {"model": ErrorResponse}},
    summary="Genera texto Lorem Ipsum",
    description="Genera texto Lorem Ipsum personalizable con opciones de formato"
)
async def generate_lorem_ipsum(request: LoremIpsumRequest):
    """
    Genera texto Lorem Ipsum personalizado basado en los parámetros proporcionados.
    
    - **paragraphs**: Número de párrafos a generar
    - **min_words**: Mínimo de palabras por párrafo
    - **max_words**: Máximo de palabras por párrafo
    - **start_with_lorem**: Si el primer párrafo debe comenzar con "Lorem ipsum dolor sit amet"
    """
    try:
        # Validar rango de palabras
        request.validate_word_range()
        
        # Generar texto Lorem Ipsum
        generated_text = lorem_generator.generate_text(
            paragraphs=request.paragraphs,
            min_words=request.min_words,
            max_words=request.max_words,
            start_with_lorem=request.start_with_lorem
        )
        
        # Contar palabras totales
        total_words = sum(len(paragraph.split()) for paragraph in generated_text.split("\n\n"))
        
        # Crear respuesta
        return LoremIpsumResponse(
            text=generated_text,
            paragraphs=request.paragraphs,
            total_words=total_words
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/generate", 
    response_model=LoremIpsumResponse,
    responses={400: {"model": ErrorResponse}},
    summary="Genera texto Lorem Ipsum (GET)",
    description="Versión GET para generar texto Lorem Ipsum personalizable"
)
async def generate_lorem_ipsum_get(
    paragraphs: int = Query(1, ge=1, description="Número de párrafos a generar"),
    min_words: int = Query(5, ge=1, description="Mínimo de palabras por párrafo"),
    max_words: int = Query(20, ge=5, description="Máximo de palabras por párrafo"),
    start_with_lorem: bool = Query(True, description="Si debe comenzar con 'Lorem ipsum dolor sit amet'")
):
    """
    Genera texto Lorem Ipsum personalizado usando parámetros de consulta GET.
    
    Útil para pruebas rápidas o para acceder a la API directamente desde un navegador.
    """
    # Crear objeto de solicitud
    request = LoremIpsumRequest(
        paragraphs=paragraphs,
        min_words=min_words,
        max_words=max_words,
        start_with_lorem=start_with_lorem
    )
    
    # Reutilizar la lógica del endpoint POST
    return await generate_lorem_ipsum(request)