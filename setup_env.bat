@echo off
REM Setup Python virtual environment and install dependencies
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install streamlit unstructured[local-inference,pdf,image,docx] pytesseract pdf2image python-docx sentence-transformers faiss-cpu crewai

REM Check for Tesseract
where tesseract >nul 2>nul
if %errorlevel% neq 0 (
    echo Tesseract not found! Please install from https://github.com/UB-Mannheim/tesseract/wiki and add to PATH.
    pause
)

REM Check for Poppler
where pdftoppm >nul 2>nul
if %errorlevel% neq 0 (
    echo Poppler not found! Please install from https://github.com/oschwartz10612/poppler-windows/releases/ and add to PATH.
    pause
)

REM Check for Ollama
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo Ollama not found! Please install from https://ollama.com/ and add to PATH.
    pause
) else (
    ollama pull qwen/qwen3:1.7b
) 