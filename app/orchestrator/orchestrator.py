from app.memory.memory_store import MemoryStore
from app.llm.mistral_client import generate_response
from app.graph.memory_graph import memory_graph

from app.memory.compressor import extract_triplet
from app.memory.wiki_store import WikiStore
from app.memory.summarizer import SummaryStore

from app.retriever.retriever import retrieve_context


async def run_orchestrator(message):

    # retrieve memories
    retrieved = retrieve_context(message)

    recent_context = retrieved["recent_memory"]
    wiki_memory = retrieved["wiki_memory"]
    summary_memory = retrieved["summary_memory"]

    # build llm context
    context = f"""
    Wiki Memory:
    {wiki_memory}

    Summary Memory:
    {summary_memory}

    Recent Context:
    {recent_context}
    """

    # generate response
    response = await generate_response(
        context=context,
        message=message
    )

    # save raw chat
    MemoryStore.add_event({
        "message": message,
        "response": response
    })

    # update rolling summaries
    SummaryStore.update(message)

    # extract graph triplets
    triplet = extract_triplet(message)

    print("TRIPLET:", triplet)

    if triplet:

        # graph memory
        memory_graph.add_relation(
            triplet["source"],
            triplet["relation"],
            triplet["target"]
        )

        # wiki memory
        WikiStore.update_entity(
            triplet["source"],
            triplet["relation"],
            triplet["target"]
        )

    return {
        "response": response,
        "context": recent_context,
        "wiki_memory": wiki_memory,
        "summary_memory": summary_memory,
        "graph": memory_graph.get_relations()
    }