from models.ollama_llm import OllamaLLM
from vectorstore.faiss_store import FAISSVectorStore
from embeddings.embedder import Embedder

class CrewAIAgent:
    def __init__(self, vector_dim=384):
        self.llm = OllamaLLM()
        self.vectorstore = FAISSVectorStore(vector_dim)
        self.embedder = Embedder()

    def ingest(self, chunks):
        embeddings = self.embedder.embed(chunks)
        self.vectorstore.add(embeddings, chunks)

    def query(self, question, top_k=5):
        q_emb = self.embedder.embed([question])[0]
        retrieved = self.vectorstore.search(q_emb, top_k=top_k)
        context = '\n'.join([text for text, _ in retrieved])
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        return self.llm.generate(prompt) 