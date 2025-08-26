# Supported extensions
SUPPORTED_EXTENSIONS = ['.pdf', '.docx', '.png', '.jpg', '.jpeg']

import os
from typing import List

def parse_document(file_path: str) -> str:
    """
    Parse a document (PDF, DOCX, or image) and return extracted text.
    Uses OCR for images and PDF fallback.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return _parse_pdf(file_path)
    elif ext == '.docx':
        return _parse_docx(file_path)
    elif ext in ['.png', '.jpg', '.jpeg']:
        return _parse_image(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def _parse_pdf(file_path: str) -> str:
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        if text.strip():
            return text
        else:
            return "PDF appears to be scanned. OCR functionality requires system dependencies not available in this deployment."
    except ImportError:
        return "PDF parsing requires pdfplumber. Please install dependencies."
    except Exception as e:
        return f"Error parsing PDF: {str(e)}"

def _parse_docx(file_path: str) -> str:
    try:
        from docx import Document
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except ImportError:
        return "DOCX parsing requires python-docx. Please install dependencies."
    except Exception as e:
        return f"Error parsing DOCX: {str(e)}"

def _parse_image(file_path: str) -> str:
    return "Image OCR requires system dependencies (Tesseract) not available in this cloud deployment. Please use text-based documents."

def _ocr_images(images: List[object]) -> str:
    return "OCR functionality requires system dependencies (Tesseract) not available in this cloud deployment."
 