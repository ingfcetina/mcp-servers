# GitHub Copilot Custom Instructions

## Project Overview

Este repositorio contiene el código fuente para desplegar y mantener un servidor `mcp-server` escrito en Python. El servidor es responsable de gestionar procesos de comunicación y procesamiento de datos con unagente de IA.

## Objetivo de las instrucciones

Estas instrucciones personalizadas están diseñadas para ayudar a GitHub Copilot (modo agente) a generar código, sugerencias y documentación relevante para este proyecto, siguiendo las mejores prácticas y convenciones del equipo.

## Reglas y convenciones

- utiliza uv para la gestión de entornos virtuales
- Python Version 3.10, 3.11, 3.12, 3.13
- Usa `logging` para la gestión de logs, no `print`.
- Utiliza `conda` para la gestión de entornos virtuales.
- Las dependencias se gestionan con uv.
- Los tests unitarios deben escribirse usando `pytest`.
- Incluye ejemplos de uso en los docstrings de las funciones principales.
- Usa tipado estático y anotaciones de tipo para mejorar la legibilidad y mantenibilidad del código.
- Mantén el código modular y reutilizable, evitando la duplicación de código.
- Implementa un manejo de errores robusto y claro, utilizando excepciones personalizadas cuando sea necesario.
- Asegúrate de que el código sea fácil de entender y mantener, utilizando nombres descriptivos para variables y funciones.
- Mantén la documentación actualizada y clara, incluyendo ejemplos de uso y explicaciones de las funciones y clases.
- Utiliza `type hints` para mejorar la legibilidad y facilitar la comprensión del código.
- Implementa pruebas unitarias y de integración para asegurar la calidad del código y su correcto funcionamiento.
- Asegúrate de que el código siga las mejores prácticas de seguridad y rendimiento.
- Mantén un estilo de codificación consistente en todo el proyecto, siguiendo las guías de estilo de Python y las convenciones del equipo.
- Utiliza `black` o `autopep8` para formatear el código automáticamente y mantener un estilo consistente.
- Implementa un sistema de gestión de configuración para manejar diferentes entornos (desarrollo, pruebas, producción) de manera eficiente y segura.
- Utiliza `dotenv` para gestionar variables de entorno y configuraciones sensibles de manera segura.
- Implementa un sistema de logging estructurado y configurable para facilitar la depuración y el monitoreo del servidor.
                             
## Buenas prácticas

- Valida y sanitiza todas las entradas externas.
- Maneja excepciones de forma explícita.
- Documenta las funciones y clases públicas.
- Prefiere la composición sobre la herencia cuando sea posible.
- Mantén el código modular y reutilizable.







