# Walkthrough: MiniProyecto Gemini

Este documento resume el desarrollo del cliente de chat con Gemini API.

## Cambios Realizados

### 1. Configuración del Proyecto
- Se creó la estructura de carpetas y archivos básicos.
- Archivo `requirements.txt` con `google-generativeai` y `python-dotenv`.
- Archivo `.env` para manejo seguro de la API Key.
- Archivo `.gitignore` para excluir credenciales y entorno virtual.

### 2. Implementación (`main.py`)
- Script principal que conecta con la API de Gemini.
- **Refactorización**: Se separó la lógica de conexión (`configure_gemini`) del bucle principal para facilitar pruebas.
- **Manejo de Modelos**: Se implementó una detección automática y fallback a `gemini-2.5-flash` (o compatible).
- **Memoria de Chat**: Se actualizó a `start_chat` para permitir conversaciones continuas con historial.

### 3. Pruebas (`test.py`)
- Se creó un script de pruebas unitarias (`unittest`) para validar:
    - La conexión correcta con la API.
    - La generación de contenido real (opcional).

## Cómo Ejecutar

### Programa Principal
Desde la raíz del proyecto:
```powershell
python -m src.main
```

### Ejecutar Pruebas
```powershell
python -m unittest discover tests
```

## Resultados de Verificación
- [x] Conexión establecida con éxito.
- [x] Pruebas unitarias pasando correctamente.
- [x] Chat interactivo funcional con memoria de contexto.
