from src.core.search import web_search
from src.core.scraper import extract_content
from src.core.embedder import embed_articles 
from src.core.vectorstore import store_embeddings
from src.agents.research_agent import answer_question
from src.llm.formatter import format_paper
from sentence_transformers import SentenceTransformer

def route_question(question: str) -> dict:
    # Step 1: Get URLs from search engine
    urls = web_search(question)
    
    # Step 2: Extract content from URLs
    articles = extract_content(urls)
    
    # Step 3: Embed and store articles for retrieval
    chunk_data = embed_articles(articles)
    store_embeddings(chunk_data)
    
    # Step 4: Generate answer using LLM
    answer, sources = answer_question(question)
    
    # Step 5: Format into a research paper
    # If sources is empty or doesn't contain URLs, use the original URLs
    source_urls = [source.get('url') for source in sources if source.get('url')] if sources else urls
    
    # Ensure we have some sources
    if not source_urls:
        source_urls = urls
        
    paper = format_paper(question, answer, source_urls)
    
    return paper