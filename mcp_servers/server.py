import os
import logging
from datetime import datetime
from typing import List, Literal
import yaml
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp_server")

# Cargar configuración YAML
def load_config(path: str = "config.yaml") -> dict:
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        return {}

config = load_config(os.path.join(os.path.dirname(__file__), "config.yaml"))

def sanitize_directory(directory: str) -> str:
    """Sanitiza y valida la ruta del directorio."""
    if not directory:
        return config.get("files", {}).get("default_directory", ".")
    # Evita rutas peligrosas
    directory = os.path.abspath(directory)
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise ValueError("Directorio no encontrado o inválido")
    return directory

class FileInfo(BaseModel):
    """
    Modelo de información de archivo para el recurso MCP.
    """
    name: str = Field(..., description="Nombre del archivo o directorio")
    size: int = Field(..., description="Tamaño en bytes")
    modified: datetime = Field(..., description="Fecha de última modificación")
    type: Literal["file", "directory"] = Field(..., description="Tipo: archivo o directorio")
    permissions: str = Field(..., description="Permisos en formato octal (ej: 0o755)")


def get_file_info(entry: os.DirEntry) -> FileInfo:
    """
    Obtiene la información relevante de un archivo o directorio.
    Args:
        entry (os.DirEntry): Entrada de directorio.
    Returns:
        FileInfo: Modelo con la información del archivo.
    """
    stat_result = entry.stat()
    return FileInfo(
        name=entry.name,
        size=stat_result.st_size,
        modified=datetime.fromtimestamp(stat_result.st_mtime),
        type="directory" if entry.is_dir() else "file",
        permissions=oct(stat_result.st_mode & 0o777)
    )

# Crear el servidor MCP
mcp = FastMCP("FileListerMCP")

@mcp.resource("files://list")
def list_default_dir() -> list[FileInfo]:
    """
    Lista los archivos del directorio por defecto configurado.

    Returns:
        list[FileInfo]: Lista de archivos y sus propiedades.

    Ejemplo de uso:
        files://list
    """
    try:
        dir_path = sanitize_directory(None)
        with os.scandir(dir_path) as entries:
            return [get_file_info(entry) for entry in entries]
    except Exception as e:
        logger.error(f"Error al listar archivos: {e}")
        raise

@mcp.resource("files://list/{directory}")
def list_files(directory: str) -> list[FileInfo]:
    """
    Lista los archivos de un directorio específico.

    Args:
        directory (str): Ruta del directorio a listar.

    Returns:
        list[FileInfo]: Lista de archivos y sus propiedades.

    Ejemplo de uso:
        files://list/tmp
    """
    try:
        dir_path = sanitize_directory(directory)
        with os.scandir(dir_path) as entries:
            return [get_file_info(entry) for entry in entries]
    except Exception as e:
        logger.error(f"Error al listar archivos: {e}")
        raise

# No se expone FastAPI ni uvicorn directamente, el SDK MCP se encarga del despliegue.
if __name__ == "__main__":
    mcp.run()