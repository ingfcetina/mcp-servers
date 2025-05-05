# server.py
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Sticky notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "sticky_notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str: 
    """
    Add a note to the sticky notes file.

    Args:
        message (str): The note to add.
    Returns:
        str: Confirmation message.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return f"Note added: {message}"

@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the sticky notes file.
    Returns:
        str: All notes, if not exists any, return "No notes found."
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content if content else "No notes found."
@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the sticky notes file.
    Returns:
        str: The latest note, if not exists any, return "No notes found."
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes found."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize the notes.
    Returns:
        str: A prompt string that includes all notes and ask for a sumamry.
        If no notes exist, return "No notes found."
    """


    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes found."
    return f"Summarize the following notes:\n{content}"
