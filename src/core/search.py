import os
from dotenv import load_dotenv
from tavily import TavilyClient
from typing import List

load_dotenv()


def web_search(query: str) -> List[str]:
    
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        raise ValueError("Tavily API Key error.")

    tavily_client = TavilyClient(api_key=tavily_key)

    # query
    try:
        response = tavily_client.search(
            query=query,
            max_results=10,
            search_depth="advanced",
            include_answer=False
        )
    except Exception as error:
        raise RuntimeError(f"Tavily API call failed: {error}")
    
    # extract url
    urls = [item["url"] for item in response.get("results", []) if "url" in item]

    return urls