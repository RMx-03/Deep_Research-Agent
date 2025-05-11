import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
from src.core.router import route_question

# Set page configuration
st.set_page_config(
    page_title="Deep Research Agent", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for academic paper styling
st.markdown("""
<style>
    .main-content {
        font-family: 'Times New Roman', Times, serif;
        line-height: 1.5;
        text-align: justify;
    }
    h1 {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    h2 {
        font-size: 20px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 1px solid #ddd;
        padding-bottom: 5px;
    }
    h3 {
        font-size: 18px;
        font-weight: bold;
        margin-top: 20px;
    }
    .reference {
        padding-left: 25px;
        text-indent: -25px;
        font-size: 14px;
    }
    .abstract {
        font-style: italic;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Deep Research Agent")
st.markdown("Ask research questions - get a structured AI-generated paper!")

question = st.text_input("Ask your research question:")

if st.button("Generate") and question:
    with st.spinner("Researching and generating academic paper..."):
        paper = route_question(question)

    # Create paper container with academic styling
    with st.container():
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        
        # Title
        st.markdown(f"<h1>{paper['title']}</h1>", unsafe_allow_html=True)
        
        # Abstract
        st.markdown("## Abstract")
        st.markdown(f'<div class="abstract">{paper["abstract"]}</div>', unsafe_allow_html=True)
        
        # Introduction
        st.markdown("## Introduction")
        st.markdown(paper["introduction"])
        
        # Main Content (already has markdown formatting)
        st.markdown(paper["body"])
        
        # Conclusion
        st.markdown("## Conclusion")
        st.markdown(paper["conclusion"])
        
        # References
        st.markdown("## References")
        for i, url in enumerate(paper["citations"], 1):
            st.markdown(f'<div class="reference">[{i}] <a href="{url}" target="_blank">{url}</a></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Add download button
    paper_text = f"""# {paper['title']}

## Abstract
{paper['abstract']}

## Introduction
{paper['introduction']}

{paper['body']}

## Conclusion
{paper['conclusion']}

## References
"""
    for i, url in enumerate(paper["citations"], 1):
        paper_text += f"[{i}] {url}\n"
        
    st.download_button(
        label="Download Paper as Markdown",
        data=paper_text,
        file_name="research_paper.md",
        mime="text/markdown"
    )