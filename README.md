# Local Document QA with OCR, Embeddings, and LLM (Qwen3:1.7b)

## Project Overview
A local, privacy-first document QA system. Upload PDFs, images, or DOCX files, which are parsed (with OCR fallback), chunked, embedded, indexed, and queried using a local LLM (Qwen3:1.7b via Ollama). No data leaves your machine.

---

## Step 0: Prerequisites
- **Python 3.9+**
- **16GB RAM** (recommended)
- **GPU** (optional, for better performance)

---

## Step 1: Setup Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

---

## Step 2: Install Python Dependencies
```bash
pip install --upgrade pip
pip install streamlit unstructured[local-inference,pdf,image,docx] pytesseract pdf2image python-docx sentence-transformers faiss-cpu crewai
```

---

## Step 3: Install System Dependencies (Windows)
- **Tesseract**: [Download](https://github.com/UB-Mannheim/tesseract/wiki)
- **Poppler**: [Download](https://github.com/oschwartz10612/poppler-windows/releases/)
- Add both to your system PATH.

---

## Step 4: Install and Setup Ollama
- [Download Ollama](https://ollama.com/)
- Verify install:
  ```bash
  ollama --version
  ```
- Pull Qwen3:1.7b model:
  ```bash
  ollama pull qwen/qwen3:1.7b
  ```

---

## Step 5: Project Structure
```
OCR/
├── app/
├── agent/
├── parsers/
├── embeddings/
├── vectorstore/
├── models/
├── data/
│   └── uploads/
├── text/
├── venv/
├── README.md
```

---

## Step 6: Running the App
```bash
streamlit run app/app.py
```
Open the local URL provided by Streamlit.

---

## User Guidance
- **Upload**: PDF, image, or DOCX files.
- **Query**: Ask questions about your documents.
- **Privacy**: All processing is local. No external API calls.

---

## Advanced Features (Optional)
- Persistent vector store
- User authentication
- Logging/monitoring
- Dockerfile for deployment 