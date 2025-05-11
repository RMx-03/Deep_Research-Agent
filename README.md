# 🧠 Deep Research Agent

An **agentic AI-powered research assistant** that autonomously plans, searches, and generates structured answers with live references — designed to help students, researchers, and developers streamline complex research using free and open tools.

---

## 🚀 What is Deep Research Agent?

The **Deep Research Agent** is a multi-step AI tool that goes beyond basic search. It uses a dual-agent architecture to understand your query, decompose it into logical sub-tasks, retrieve real-time web results, and respond with coherent, reliable insights — all inside a simple, interactive UI.

Whether you're writing a research paper or exploring a technical topic, this assistant can help you **save hours of manual Googling and summarizing**.

---

## 💡 Key Features

- 🧭 **Dual-Agent Reasoning**: Uses a planner-executor agent structure powered by LangChain.
- 🔍 **Live Web Search**: Retrieves up-to-date data using Tavily's no-cost API.
- ✍️ **Natural Language Responses**: Cohere's language model generates rich, contextual answers.
- 📂 **Document-Aware Search**: Upload PDFs or text files for context-specific Q&A.
- 🖥️ **Streamlit UI**: Clean, simple front-end for research interaction.
- 📊 **Answer Evaluation**: Integrated with DeepEval to measure answer quality and coherence.

---

## 🛠️ Tech Stack

- `Python`
- `LangChain`
- `Streamlit`
- `Tavily API`
- `Cohere API`
- `OpenAI API` 
- `DeepEval` 

---

## 🧰 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/deep-research-agent.git
   cd deep-research-agent
   ```
   
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
     
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Configure your API keys**
   Create a .env file in the root directory:
   ```bash
   COHERE_API_KEY=your_cohere_api_key
   TAVILY_API_KEY=your_tavily_api_key
   OPENAI_API_KEY=your_optional_openai_key
   ```
      
5. **Run the Streamlit app**
   ```bash
   streamlit run src/ui/app.py
   ```

---

## 📁 Project Structure
   ```bash
   deep-research-agent/
   │
   ├── src/
   │ ├──agents/ # agent execution
   │ ├── core/ # Core logic: planning, routing 
   │ ├── ui/ # Streamlit-based UI
   │ ├── llm/ # Helper 
   │
   ├── main.py
   ├── chroma_store/ # Local Storage
   ├── .env.example # Example environment config
   ├── requirements.txt # Python dependencies
   └── README.md
   ```

---

## 🌍 Use Cases

- 📚 Generating academic research content  
- 🧪 Technical exploration or topic breakdown  
- 🤖 AI-assisted learning and discovery  
- 📄 Automated summarization and document Q&A  

---

## 📌 Limitations

- ⛔ Built on free-tier APIs (rate-limited)  
- 🌐 Currently supports English-only queries  
- 🔍 Web search limited by Tavily’s scope and filters  

---

## 🤝 Contributions

Want to improve this tool? Feel free to **fork**, **submit issues**, or **open a PR**!  
Ideas for improvement:

- 🧠 Add vector DB support  
- 📚 Plug in academic sources (e.g., arXiv, Semantic Scholar)  
- 💾 Offline mode or response caching  

---

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)  
- [Tavily](https://www.tavily.com/)  
- [Cohere](https://cohere.ai/)  
- [Streamlit](https://streamlit.io/)  
- [DeepEval](https://github.com/confident-ai/deepeval)  
