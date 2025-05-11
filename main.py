# from src.core.search import web_search
# from src.core.scraper import extract_content
# from src.core.embedder import embed_articles
# from src.core.vectorstore import store_embeddings


# user_question = "what is the use of agentic ai?"
# urls = web_search(user_question)
# articles = extract_content(urls)
# chunk_data = embed_articles(articles)
# store_embeddings(chunk_data)

from src.core.router import route_question

def main():
    user_question = "what is the use of agentic ai?"
    paper = route_question(user_question)
    
    print("=" * 80)
    print(f"TITLE: {paper['title']}")
    print("=" * 80)
    
    print("ABSTRACT:")
    print(paper['abstract'])
    print("=" * 80)
    
    print("INTRODUCTION:")
    print(paper['introduction'])
    print("=" * 80)
    
    print("MAIN CONTENT:")
    print(paper['body'])
    print("=" * 80)
    
    print("CONCLUSION:")
    print(paper['conclusion'])
    print("=" * 80)
    
    print("REFERENCES:")
    for i, url in enumerate(paper["citations"], 1):
        print(f"[{i}] {url}")
    print("=" * 80)

if __name__ == "__main__":
    main()