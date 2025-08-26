# OCRContext - Railway Deployment

## Local Development
```bash
git clone https://github.com/deepakchoudhary-dc/OCRContext-
cd OCRContext-
pip install -r requirements.txt
streamlit run app/app.py
```

## Railway Deployment

### Option 1: One-Click Deploy
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

### Option 2: Manual Deploy
1. Connect your GitHub repo to Railway
2. Railway will automatically detect the `Dockerfile` and `railway.json`
3. Deploy will start automatically

### Option 3: Railway CLI
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Environment Variables (Optional)
- `OLLAMA_HOST`: Set to external Ollama instance if needed (default: http://localhost:11434)

## Notes
- OCR functionality works on Railway (Tesseract included)
- Document parsing for PDF/DOCX works fully
- LLM functionality requires either:
  - External Ollama instance (set OLLAMA_HOST)
  - Or will show fallback message for demo purposes

## System Requirements on Railway
- Memory: 1GB+ recommended
- Disk: 2GB+ for dependencies
- Network: Outbound HTTP for external LLM (if used)
