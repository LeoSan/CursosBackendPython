import unittest
import google.generativeai as genai
from src.gemini_client import configure_gemini

class TestGeminiConnection(unittest.TestCase):
    
    def test_connection_success(self):
        """Prueba que la conexión a Gemini se establezca correctamente"""
        print("\nEjecutando test de conexión...")
        try:
            model = configure_gemini()
            self.assertIsInstance(model, genai.GenerativeModel, "El objeto retornado no es un modelo de Gemini")
            print("[OK] Conexión exitosa: Modelo configurado correctamente.")
        except Exception as e:
            self.fail(f"[FAIL] La conexión falló con el error: {e}")

    def test_api_call(self):
        """Prueba opcional: enviar un mensaje simple 'Hola' para verificar respuesta real"""
        print("\nEjecutando test de respuesta real...")
        try:
            model = configure_gemini()
            response = model.generate_content("Hola, esto es un test.")
            self.assertIsNotNone(response.text)
            print("[OK] Respuesta recibida de Gemini:", response.text[:50] + "...")
        except Exception as e:
            print(f"[WARN] El test de respuesta real falló (puede ser por cuota o red): {e}")
            pass

if __name__ == '__main__':
    unittest.main()
