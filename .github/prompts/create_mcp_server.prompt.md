# Prompt: Crear un MCP Server en Python para listar archivos de un directorio

Tu objetivo es generar código, sugerencias y documentación para crear un servidor MCP (Model context protocol) en Python que permita crear recursos para crear un archivo de notas, resumirlo, agregar notas y obtener la última nota. Utilizando la guía oficial del SDK: https://github.com/modelcontextprotocol/python-sdk

## Requerimientos técnicos

- Python 3.10 o superior
- Uso de uv para gestión de entornos virtuales y dependencias
- Implementación del SDK MCP siguiendo la documentación oficial
- Logging estructurado y configurable
- Manejo robusto de errores con excepciones personalizadas
- Tipado estático completo
- Documentación con docstrings y ejemplos de uso

## Estructura del proyecto

mcp-servers/
  ├── CONTRIBUTING.md
  ├── LICENSE
  ├── README.md
  ├── requirements.txt
  └── project/
      ├── main.py
      ├── pyproject.toml
      ├── README.md
      ├── sticky_notes.txt
      ├── uv.lock
      └── __pycache__/
          ├── main.cpython-313.pyc
          └── test.cpython-313.pyc

## Funcionalidades requeridas

1. **Recursos MCP:**
   - `notes://create` - Crear un nuevo archivo de notas
   - `notes://list` - Listar todas las notas existentes
   - `notes://get/{id}` - Obtener una nota específica por su ID

2. **Herramientas MCP:**
   - `add_note(message: str)` - Agregar una nueva nota
   - `summarize_notes()` - Generar un resumen de todas las notas
   - `get_latest_note()` - Obtener la nota más reciente

3. **Características adicionales:**
   - Persistencia de datos en archivo
   - Validación de entradas
   - Formato JSON para intercambio de datos
   - Manejo de errores personalizado

## Ejemplos de uso

El servidor debe permitir interacciones como:

```
# Agregar una nota
add_note("Reunión con el equipo de desarrollo el viernes a las 10:00")

# Obtener todas las notas
notes://list

# Resumir todas las notas
summarize_notes()
```

## Consideraciones de seguridad y rendimiento

- Implementar sanitización de entradas para evitar inyecciones
- Manejar permisos de acceso a archivos del sistema
- Optimizar para respuestas rápidas
- Implementar mecanismos para manejar carga elevada

## Integración y pruebas

- Incluir ejemplos de cómo usar el servidor con clientes MCP
- Implementar pruebas unitarias con pytest
- Documentar el proceso de instalación y ejecución

## Referencias

- Documentación oficial MCP: https://github.com/modelcontextprotocol/python-sdk
- Especificación MCP: https://modelcontextprotocol.io



