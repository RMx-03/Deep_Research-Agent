import uuid
import chromadb
from chromadb.config import Settings
from typing import List, Tuple, Dict
from src.core.embedder import embed_articles

client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection(name="research_chunks")

def store_embeddings(embedded_chunks: List[Tuple[str, str, List[float]]]) -> None:
    for url, chunk_text, embedding in embedded_chunks:
        unique_id = str(uuid.uuid4())
        collection.add(
            ids=[unique_id],
            documents=[chunk_text],
            embeddings=[embedding],
            metadatas=[{"url": url}]
        )

def add_documents_to_vectorstore(documents: List[Dict[str, str]]) -> None:
    texts = [doc['text'] for doc in documents]
    urls = [doc['url'] for doc in documents]
    embeddings = embed_articles(texts)

    embedded_chunks = list(zip(urls, texts, embeddings))
    store_embeddings(embedded_chunks)

def get_similar_chunks(query_embedding: List[float], top_k: int = 5) -> List[Dict]:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=['documents', 'embeddings', 'metadatas', 'distances']
    )

    chunks = []
    for doc, meta, distance in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        chunks.append({
            "text": doc,
            "url": meta["url"],
            "score": 1 - distance
        })

    return chunks