from typing import Dict, List, Tuple
from sentence_transformers import SentenceTransformer
import re

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def embed_articles(articles: Dict[str, str]) -> List[Tuple[str, str, List[float]]]:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_data = []

    for url, text in articles.items():
        cleaned_text = clean_text(text)
        chunks = split_chunks(cleaned_text)

        for chunk in chunks:
            embedding = model.encode(chunk).tolist()
            chunk_data.append((url, chunk, embedding))

    return chunk_data