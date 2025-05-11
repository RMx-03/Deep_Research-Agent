import time
from typing import List, Dict
from newspaper import Article

def extract_content(urls: List[str]) -> Dict[str, str]:
    extracted_content = {}

    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text.strip()
            extracted_content[url] = text
            time.sleep(2)
        except Exception as error:
            print(f"Error in Extracting Content: {error}")
            continue

    return extracted_content