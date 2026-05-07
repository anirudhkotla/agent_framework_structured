import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)

MEMORY_FILE = DATA_DIR / "memory.json"

if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("[]")


class MemoryStore:

    @staticmethod
    def load_memory():

        with open(MEMORY_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []

    @staticmethod
    def save_memory(memory):

        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)

    @staticmethod
    def add_event(event):

        memory = MemoryStore.load_memory()

        memory.append(event)

        MemoryStore.save_memory(memory)