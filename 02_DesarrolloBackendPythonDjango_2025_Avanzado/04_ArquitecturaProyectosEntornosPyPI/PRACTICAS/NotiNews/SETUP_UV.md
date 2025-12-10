# Guía de Inicio Rápido con `uv` 🚀

Esta guía te ayudará a configurar y ejecutar el proyecto **NotiNews** utilizando `uv`, un gestor de paquetes de Python extremadamente rápido.

## 1. Prerrequisitos

Asegúrate de tener instalado **Python 3.13** o superior.

## 2. Instalar `uv`

Si aún no tienes `uv` instalado, abre tu terminal (PowerShell en Windows) y ejecuta:

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS y Linux
Si usas **Homebrew**, es muy sencillo:
```bash
brew install uv
```

O si prefieres el script oficial:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> [!IMPORTANT]
> **Si ves un error de "Execution Policy"**:
> Windows bloquea la ejecución de scripts de instalación por seguridad. Para solucionarlo, ejecuta este comando y luego intenta instalar de nuevo:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -scope CurrentUser
> ```

> [!TIP]
> **Si ves el error "El término 'uv' no se reconoce"**:
> Esto sucede porque la instalación terminó pero tu terminal actual no ha actualizado sus rutas (PATH).
> **Solución**: Cierra esta ventana de PowerShell y abre una nueva.

## 3. Configuración del Proyecto

Ve a la carpeta raíz del proyecto:

```powershell
cd ruta\a\NotiNews
```

### 3.1 Inicializar el entorno virtual
Crea un entorno virtual nuevo. `uv` usará automáticamente la versión de Python definida en `.python-version` o la más reciente disponible.

```bash
uv venv
```

### 3.2 Instalar dependencias
Instala el proyecto y sus dependencias en modo editable. Este paso es **CRUCIAL** para que el comando `noti-news` funcione.

```bash
uv pip install -e .
```

*Esto leerá el archivo `pyproject.toml` e instalará todas las librerías necesarias como `google-generativeai`, `requests`, y `rich`.*

## 4. Configurar Variables de Entorno

Asegúrate de tener un archivo `.env` en la raíz del proyecto con tus claves de API válidas.

Ejemplo de contenido para `.env`:

```env
# Claves REQUERIDAS
NEWSAPI_API_KEY=tu_api_key_de_newsapi
GOOGLE_API_KEY=tu_api_key_de_google_gemini

# Configuraciones Opcionales
GEMINI_MODEL=gemini-2.5-flash
MAX_ARTICLES=10
```

## 5. Ejecutar la Aplicación

Ahora puedes usar `uv run` para ejecutar la aplicación sin necesidad de activar manualmente el entorno virtual (`activate`).

### Buscar noticias
```bash
uv run noti-news search "Python 3.13"
```

### Preguntar sobre noticias (con IA)
```bash
uv run noti-news ask "Inteligencia Artificial" "¿Qué novedades hay?"
```
### Ejecutar TESTS (con IA)
```bash
uv run python -m unittest discover tests
```

## Solución de Problemas Comunes

- **"Failed to spawn: noti-news"**: Significa que olvidaste ejecutar `uv pip install -e .`. El entorno virtual existe pero el proyecto no está instalado dentro de él.
- **"ModuleNotFoundError: No module named 'noti_news'"**: Igual que el anterior, reinstala con `uv pip install -e .`.
- **Error de API Key**: Verifica que las claves en `.env` sean correctas y no tengan espacios extra al final.
