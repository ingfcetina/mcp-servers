# GitHub Copilot Custom Instructions

## Project Overview

Este repositorio contiene el código fuente para desplegar y mantener un servidor `mcp-server` escrito en Python. El servidor es responsable de gestionar procesos de comunicación y procesamiento de datos para aplicaciones internas.

## Objetivo de las instrucciones

Estas instrucciones personalizadas están diseñadas para ayudar a GitHub Copilot (modo agente) a generar código, sugerencias y documentación relevante para este proyecto, siguiendo las mejores prácticas y convenciones del equipo.

## Reglas y convenciones

- El código debe estar escrito en Python 3.8 o superior.
- Utiliza `conda` para la gestión de entornos virtuales.
- La instalación del python base esta en C:\Program Files\ArcGIS\Pro\bin\Python y es una instalación de ArcGIS Pro.
- Sigue la convención de nombres PEP8.
- Los endpoints deben documentarse usando docstrings y, si aplica, OpenAPI (Swagger).
- Usa `logging` para la gestión de logs, no `print`.
- Utiliza `conda` para la gestión de entornos virtuales.
- Las dependencias se gestionan en `requirements.txt` y se instalan con `conda`, si no están disponibles en conda se usa `pip`.
- Los tests unitarios deben escribirse usando `pytest`.
- El servidor se despliega usando `uvicorn` o `gunicorn` según el entorno.
- Incluye ejemplos de uso en los docstrings de las funciones principales.
- Usa tipado estático y anotaciones de tipo para mejorar la legibilidad y mantenibilidad del código.
- Mantén el código modular y reutilizable, evitando la duplicación de código.
- Utiliza `async` y `await` para operaciones de I/O asíncronas cuando sea posible.
- Implementa un manejo de errores robusto y claro, utilizando excepciones personalizadas cuando sea necesario.
- Asegúrate de que el código sea fácil de entender y mantener, utilizando nombres descriptivos para variables y funciones.
- Mantén la documentación actualizada y clara, incluyendo ejemplos de uso y explicaciones de las funciones y clases.
- Utiliza `type hints` para mejorar la legibilidad y facilitar la comprensión del código.
- Implementa pruebas unitarias y de integración para asegurar la calidad del código y su correcto funcionamiento.
- Asegúrate de que el código siga las mejores prácticas de seguridad y rendimiento.
- Utiliza herramientas de análisis estático y linters para mantener la calidad del código y detectar problemas potenciales antes de que se conviertan en errores.
- Mantén un estilo de codificación consistente en todo el proyecto, siguiendo las guías de estilo de Python y las convenciones del equipo.
- Utiliza `black` o `autopep8` para formatear el código automáticamente y mantener un estilo consistente.
- Implementa un sistema de gestión de configuración para manejar diferentes entornos (desarrollo, pruebas, producción) de manera eficiente y segura.
- Utiliza `dotenv` para gestionar variables de entorno y configuraciones sensibles de manera segura.
- Implementa un sistema de logging estructurado y configurable para facilitar la depuración y el monitoreo del servidor.
- Utiliza `pydantic` para la validación de datos y la creación de modelos de datos, asegurando que los datos sean válidos y cumplan con las expectativas del servidor.
- utiliza archivos yaml para la configuración de las herramientas y el entorno del servidor, asegurando que la configuración sea fácil de leer y modificar.
                             
## Buenas prácticas

- Valida y sanitiza todas las entradas externas.
- Maneja excepciones de forma explícita.
- Documenta las funciones y clases públicas.
- Prefiere la composición sobre la herencia cuando sea posible.
- Mantén el código modular y reutilizable.

## Ejemplo de estructura de un archivo de configuración YAML

```yaml
# config.yaml
server:
  host: "localhost"
    port: 8000
    log_level: "info"
    debug: true

database:
    host: "localhost"
    port: 5432
    user: "user"
    password: "password"
    db_name: "database_name"
    max_connections: 10
    timeout: 30
    retry_attempts: 3
    retry_delay: 5
    retry_backoff_factor: 2
    retry_max_delay: 60
    retry_jitter: true
    retry_on_timeout: true
    retry_on_connection_error: true
    retry_on_server_error: true
    retry_on_client_error: true
    retry_on_network_error: true
    retry_on_database_error: true
    retry_on_protocol_error: true
    retry_on_timeout_error: true
    retry_on_connection_timeout_error: true
    retry_on_server_timeout_error: true
    retry_on_client_timeout_error: true
    retry_on_network_timeout_error: true
    retry_on_database_timeout_error: true
    retry_on_protocol_timeout_error: true

logging:
    level: "info"
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handlers:
        - type: "console"
        - type: "file"
        filename: "app.log"
        max_size: 10485760 # 10 MB
        backup_count: 5
        - type: "smtp"
        mailhost: "smtp.example.com"
        fromaddr: "
        toaddrs: [" 
        subject: "Error in MCP Server"
        credentials:
            username: "user"
            password: "password"
        secure: true
        level: "error"
        - type: "http"
        url: "http://example.com/log"
        method: "POST"
        headers:
            Content-Type: "application/json"
            level: "info"
        - type: "syslog"
        address: "localhost"
        port: 514   
        facility: "user"
        level: "info"
        - type: "tcp"
        address: "localhost"
        port: 5000
        level: "info"
        - type: "udp"
        address: "localhost"
        port: 5000
        level: "info"
        - type: "http"
        url: "http://example.com/log"
        method: "POST"
        headers:
            Content-Type: "application/json"
        level: "info"
        - type: "file"
        filename: "app.log"
        max_size: 10485760 # 10 MB
        backup_count: 5
        level: "info"
        - type: "console"
```







