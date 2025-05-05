# Prompt: Crear un MCP Server en Python para listar archivos de un directorio

Tu objetivo es generar código, sugerencias y documentación para crear un servidor MCP (Multi-Channel Processing Server) en Python que permita listar todos los archivos de un directorio y sus propiedades, siguiendo las mejores prácticas y convenciones del equipo, y utilizando la guía oficial del SDK: https://github.com/modelcontextprotocol/python-sdk

## Antes de generar código, pregunta:
- ¿Qué propiedades de los archivos se deben incluir (por ejemplo, tamaño, fecha de modificación, tipo, permisos, etc)?
- ¿El directorio debe ser configurable a través de un parámetro, variable de entorno, archivo de configuración YAML o resource?

## Requisitos para el servidor MCP:
- Usa Python 3.8 o superior.
- Utiliza el SDK oficial de MCP: [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk).
- No uses FastAPI directamente, el SDK MCP ya expone los endpoints.
- Gestiona el entorno virtual con `conda` (preferido para ArcGIS Pro) o `venv` si es necesario.
- Sigue la convención de nombres PEP8.
- Documenta los recursos y herramientas con docstrings claros y ejemplos de uso.
- Usa el módulo `logging` para logs, no uses `print`.
- Gestiona dependencias en `requirements.txt` e instala primero con `conda`, luego con `pip` si no están disponibles.
- Escribe tests unitarios con `pytest` y colócalos en la carpeta `tests/`.
- Incluye ejemplos de uso en los docstrings de las funciones principales.
- Usa tipado estático y anotaciones de tipo para mejorar la legibilidad y mantenibilidad del código.
- Mantén el código modular y reutilizable, evitando la duplicación de código.
- Implementa manejo de errores robusto y claro, utilizando excepciones personalizadas cuando sea necesario.
- Utiliza archivos YAML para la configuración y dotenv para variables sensibles.
- Implementa logging estructurado y configurable.
- Utiliza `pydantic` para la validación y modelado de datos.

## Buenas prácticas:
- Valida y sanitiza todas las entradas externas.
- Maneja excepciones de forma explícita.
- Documenta funciones y clases públicas.
- Prefiere composición sobre herencia cuando sea posible.
- Mantén el código modular y reutilizable.

## Ejemplo de un recurso MCP para listar archivos:

```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import Literal
import os
from datetime import datetime

class FileInfo(BaseModel):
    name: str
    size: int
    modified: datetime
    type: Literal["file", "directory"]
    permissions: str

mcp = FastMCP("FileListerMCP")

@mcp.resource("files://list")
def list_default_dir() -> list[FileInfo]:
    """
    Lista los archivos del directorio por defecto configurado.
    """
    dir_path = "./"  # O usa configuración YAML
    with os.scandir(dir_path) as entries:
        return [FileInfo(
            name=e.name,
            size=e.stat().st_size,
            modified=datetime.fromtimestamp(e.stat().st_mtime),
            type="directory" if e.is_dir() else "file",
            permissions=oct(e.stat().st_mode & 0o777)
        ) for e in entries]

@mcp.resource("files://list/{directory}")
def list_files(directory: str) -> list[FileInfo]:
    """
    Lista los archivos de un directorio específico.
    """
    dir_path = os.path.abspath(directory)
    with os.scandir(dir_path) as entries:
        return [FileInfo(
            name=e.name,
            size=e.stat().st_size,
            modified=datetime.fromtimestamp(e.stat().st_mtime),
            type="directory" if e.is_dir() else "file",
            permissions=oct(e.stat().st_mode & 0o777)
        ) for e in entries]
```

## Estructura recomendada del proyecto:

```
mcp-servers/
├── mcp_servers/
│   ├── __init__.py
│   ├── config.yaml
│   ├── server.py
├── requirements.txt
├── README.md
├── tests/
│   ├── __init__.py
│   └── test_server.py
```

## Ejemplo de archivo de configuración YAML

```yaml
server:
  host: "localhost"
  port: 8000
  log_level: "info"
  debug: true
files:
  default_directory: "./"
```

## Ejemplo de test con pytest

```python
import os
import tempfile
from server import list_files

def test_list_files_returns_files():
    test_dir = tempfile.mkdtemp()
    try:
        open(os.path.join(test_dir, "file1.txt"), "w").close()
        result = list_files(test_dir)
        assert any(f.name == "file1.txt" for f in result)
    finally:
        os.rmdir(test_dir)
```