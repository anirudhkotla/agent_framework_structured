from app.memory.memory_store import MemoryStore
from app.memory.wiki_store import WikiStore
from app.memory.summarizer import SummaryStore


def retrieve_context(query):

    raw_memory = MemoryStore.load_memory()

    wiki = WikiStore.load_wiki()

    summary_memory = SummaryStore.load()

    recent = raw_memory[-5:]

    return {
        "recent_memory": recent,
        "wiki_memory": wiki,
        "summary_memory": summary_memory
    }