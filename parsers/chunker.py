import re
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Advanced text chunker that splits text into paragraphs, then merges them into chunks
    of approximately `chunk_size` characters, with `overlap` between chunks for context.
    Handles edge cases for very long or very short paragraphs.
    """
    # Split into paragraphs (double newlines or single newlines with indentation)
    paragraphs = re.split(r'\n\s*\n|(?<=\n)\s{2,}', text)
    chunks = []
    current_chunk = []
    current_length = 0
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_length + len(para) + 1 > chunk_size and current_chunk:
            # Save current chunk
            chunk = '\n'.join(current_chunk)
            chunks.append(chunk)
            # Start new chunk with overlap
            if overlap > 0 and len(chunk) > overlap:
                overlap_text = chunk[-overlap:]
                current_chunk = [overlap_text, para]
                current_length = len(overlap_text) + len(para) + 1
            else:
                current_chunk = [para]
                current_length = len(para) + 1
        else:
            current_chunk.append(para)
            current_length += len(para) + 1
    # Add last chunk
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    # Remove empty or whitespace-only chunks
    chunks = [c for c in chunks if c.strip()]
    return chunks
 