import os
import cohere
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb 
from chromadb.config import Settings
from typing import List, Dict, Tuple

load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(API_KEY)

def answer_question(question: str) -> Tuple[str, List[Dict[str, str]]]:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    question_embedding = model.encode(question).tolist()

    client = chromadb.PersistentClient(path="chroma_store")
    collection = client.get_or_create_collection("research_chunks")
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=10,
        include=['documents', 'metadatas']
    )

    retrieved_chunks = results["documents"][0]
    sources = results["metadatas"][0]

    context = "\n\n".join(retrieved_chunks)
    prompt = f"""
    You are an expert academic researcher writing a comprehensive research paper.
    
    Based on the provided information, create a detailed and well-structured response to the research question.
    
    Your response should be scholarly, informative, and demonstrate critical analysis of the available information.
    Ensure proper organization with logical flow between sections.
    
    Use academic language but maintain clarity. Cite relevant information from the sources.
    If there are gaps in the available information, acknowledge them as areas for future research.
    
    Context Information:
    {context}
    
    Research Question: {question}
    
    Structure your response as a detailed academic research paper that would be suitable for publication:
    """

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7,
        stop_sequences=["--"]
    )

    source_info = []
    for source in sources:
        if source and "url" in source:
            if source["url"] not in [s["url"] for s in source_info]:
                source_info.append({"url": source["url"]})

    return response.generations[0].text.strip(), source_info