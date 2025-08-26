import streamlit as st
import os
import warnings
import logging

# Suppress torch warnings and other non-critical warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
logging.getLogger("torch").setLevel(logging.ERROR)

from parsers.document_parser import parse_document, SUPPORTED_EXTENSIONS
from parsers.chunker import chunk_text
from agent.crewai_agent import CrewAIAgent

UPLOAD_DIR = os.path.join('data', 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title('OCRContext - Document QA with Local LLM')
st.write('🚀 Upload a document and ask questions. OCR and document processing work fully on this deployment!')

# Railway deployment info
st.info('📋 **What works**: PDF text extraction, DOCX processing, OCR for images, document chunking, and semantic search. LLM responses require external Ollama or show demo message.')

if 'agent' not in st.session_state:
    st.session_state['agent'] = CrewAIAgent()
    st.session_state['ingested'] = False

uploaded_file = st.file_uploader('Upload a document (PDF, DOCX, Image)', type=[ext[1:] for ext in SUPPORTED_EXTENSIONS])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success(f'File uploaded: {uploaded_file.name}')
    with st.spinner('Parsing document...'):
        try:
            text = parse_document(file_path)
            st.success('Document parsed successfully!')
            st.text_area('Extracted Text Preview', text[:2000], height=200)
            chunks = chunk_text(text)
            st.info(f'Chunked into {len(chunks)} segments.')
            if st.button('Ingest Document'):
                with st.spinner('Generating embeddings and indexing...'):
                    st.session_state['agent'].ingest(chunks)
                    st.session_state['ingested'] = True
                st.success('Document ingested and indexed!')
        except Exception as e:
            st.error(f'Error parsing document: {e}')

if st.session_state.get('ingested', False):
    st.header('Ask a Question')
    question = st.text_input('Enter your question about the document:')
    if st.button('Get Answer') and question:
        with st.spinner('Retrieving answer from LLM...'):
            try:
                answer = st.session_state['agent'].query(question)
                if answer.startswith('Error:'):
                    st.error(f'LLM Error: {answer}')
                else:
                    st.markdown(f'**Answer:** {answer}')
            except Exception as e:
                st.error(f'Error during LLM query: {e}')
                st.info('Tip: Make sure Ollama is running and the qwen3:1.7b model is available')

st.markdown('---')
st.markdown('**Privacy Notice:** All processing (OCR, embedding, vector search, LLM) is performed locally. No data leaves your machine. No external API calls are made.') 