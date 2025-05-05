# 📝 AI Sticky Notes MCP Server

## 📋 Descripción

Este proyecto implementa un servidor MCP (Model Context Protocol) para gestionar notas adhesivas. Permite a los modelos de IA crear, leer y resumir notas almacenadas en un archivo de texto.

## 🏗️ Arquitectura

```mermaid
graph TD
    A[Cliente MCP] -->|Solicita acción| B[Servidor FastMCP]
    B -->|Herramientas| C[add_note]
    B -->|Herramientas| D[read_notes]
    B -->|Recursos| E[get_latest_note]
    B -->|Prompts| F[note_summary_prompt]
    C -->|Escribe en| G[sticky_notes.txt]
    D -->|Lee de| G
    E -->|Lee de| G
    F -->|Lee de| G
```

## 🧩 Componentes

El servidor MCP ofrece tres tipos principales de componentes:

### 🛠️ Herramientas (`@mcp.tool()`)

Las herramientas son funciones que el modelo puede invocar para realizar acciones.

```mermaid
classDiagram
    class Tool {
        +add_note(message: str) str
        +read_notes() str
    }
```

- **add_note**: Agrega una nueva nota al archivo
- **read_notes**: Lee todas las notas almacenadas

### 📚 Recursos (`@mcp.resource()`)

Los recursos proporcionan datos que el modelo puede consultar.

```mermaid
classDiagram
    class Resource {
        +get_latest_note() str
    }
```

- **get_latest_note**: Devuelve solo la nota más reciente

### 💬 Prompts (`@mcp.prompt()`)

Los prompts generan instrucciones personalizadas para el modelo de IA.

```mermaid
classDiagram
    class Prompt {
        +note_summary_prompt() str
    }
```

- **note_summary_prompt**: Crea un prompt para resumir todas las notas

## 📊 Flujo de Datos

```mermaid
sequenceDiagram
    participant AI as Modelo de IA
    participant MCP as Servidor MCP
    participant File as sticky_notes.txt
    
    AI->>MCP: Invocar add_note("Nueva nota")
    MCP->>File: Escribir "Nueva nota"
    MCP->>AI: "Note added: Nueva nota"
    
    AI->>MCP: Invocar read_notes()
    MCP->>File: Leer contenido
    MCP->>AI: "Nueva nota\nOtra nota anterior"
    
    AI->>MCP: Consultar notes://latest
    MCP->>File: Leer última línea
    MCP->>AI: "Nueva nota"
    
    AI->>MCP: Usar note_summary_prompt()
    MCP->>File: Leer contenido
    MCP->>AI: "Summarize the following notes:\nNueva nota\nOtra nota anterior"
```

## 🚀 Cómo Usar

Para usar este servidor MCP en VS Code:

1. Asegúrate de tener la extensión MCP instalada
2. Configura el servidor en settings.json:
```json
"mcp": {
    "servers": {
        "Demo": {
            "command": "uv",
            "args": [
                "run",
                "--with",
                "mcp[cli]",
                "mcp",
                "run",
                "C:\\mcp-servers\\project\\main.py"
            ]
        }
    }
}
```
3. Abre el Inspector MCP y selecciona "Demo"

## 📋 Referencia

| Tipo | Nombre | Descripción |
|------|--------|-------------|
| 🛠️ Tool | add_note | Agrega una nota al archivo |
| 🛠️ Tool | read_notes | Lee todas las notas del archivo |
| 📚 Resource | notes://latest | Obtiene la nota más reciente |
| 💬 Prompt | note_summary_prompt | Genera un prompt para resumir notas |