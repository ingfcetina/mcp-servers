# MCP Server: Listado de Archivos

Este proyecto implementa un servidor MCP en Python para listar archivos de un directorio y sus propiedades, siguiendo las mejores prácticas del equipo.

## Requisitos
- Python 3.10+
- Conda (recomendado para gestión de entornos)

## Instalación
```sh
conda create -n mcp_server_py310 python=3.10
conda activate mcp_server_py310
pip install -r requirements.txt
```

## Configuración
- Edita `config.yaml` para definir el directorio por defecto y la configuración del servidor.
- Usa `.env` para variables sensibles (ejemplo incluido).

## Ejemplo de uso
```python
from mcp.server.fastmcp import FastMCP
from server import list_files

# Listar archivos de un directorio
archivos = list_files("./")
for archivo in archivos:
    print(archivo)
```

## Despliegue
```sh
uvicorn server:mcp --host 0.0.0.0 --port 8000
```

## Pruebas
```sh
pytest test_server.py
```

## Estructura de configuración YAML
Ver ejemplo robusto en `config.yaml`.

## Buenas prácticas
- Validación y sanitización de entradas
- Logging estructurado
- Tipado estático y Pydantic
- Modularidad y tests con pytest

---

> Para más detalles, consulta la documentación interna y los comentarios en el código fuente.
