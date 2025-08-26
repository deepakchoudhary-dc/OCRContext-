import faiss
import numpy as np
from typing import List, Tuple

class FAISSVectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.embeddings = None

    def add(self, embeddings: List[List[float]], texts: List[str]):
        arr = np.array(embeddings).astype('float32')
        if self.embeddings is None:
            self.embeddings = arr
        else:
            self.embeddings = np.vstack([self.embeddings, arr])
        self.index.add(arr)
        self.texts.extend(texts)

    def search(self, query_emb: List[float], top_k: int = 5) -> List[Tuple[str, float]]:
        query = np.array(query_emb).reshape(1, -1).astype('float32')
        D, I = self.index.search(query, top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], float(dist)))
        return results
 