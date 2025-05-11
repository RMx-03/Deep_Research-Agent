# Deep Research Agent

A research assistance tool that generates structured papers from user queries by leveraging web search, web scraping, and AI-powered content generation.

## How It Works

1. User submits a research question or topic
2. The system searches the web for relevant sources using Tavily API
3. Content is extracted from the top search results using newspaper3k
4. The extracted content is embedded and stored in a vector database (ChromaDB)
5. An LLM (Cohere) uses the retrieved information to generate a structured research paper

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your API keys:
   ```
   TAVILY_API_KEY=your_tavily_api_key
   COHERE_API_KEY=your_cohere_api_key
   ```

## Usage

### CLI Mode
```
python main.py
```

### UI Mode
```
streamlit run src/ui/app.py
```

## Requirements

- Python 3.8+
- Required packages listed in requirements.txt
