import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure_gemini():
    """Configura y retorna el modelo de Gemini."""
    # 1. Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("No se encontró la variable GEMINI_API_KEY en el archivo .env")

    # 2. Configurar el API
    try:
        genai.configure(api_key=api_key)
        
        # Opcional: Listar modelos para debug (descomentar si es necesario)
        # print("Buscando modelos disponibles...")
        # for m in genai.list_models():
        #    if 'generateContent' in m.supported_generation_methods:
        #        print(f" - Encontrado: {m.name}")

        # Usamos el modelo validado en pruebas (gemini-2.5-flash)
        model_name = 'gemini-2.5-flash'
        model = genai.GenerativeModel(model_name)
        return model
    except Exception as e:
        raise ConnectionError(f"Error al configurar Gemini: {e}")
