import os
import numpy as np
import faiss
from transformers import AutoTokenizer, AutoModel
from typing import List


class RAGService:
    def __init__(self, model_name: str = "bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.index = self.build_index()

    def load_processed_texts(self) -> List[str]:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        processed_dir = os.path.join(project_root, "data", "processed")
        corpus = []
        for filename in os.listdir(processed_dir):
            if filename.endswith(".txt"):
                with open(
                    os.path.join(processed_dir, filename), "r", encoding="utf-8"
                ) as file:
                    corpus.append(file.read())
        return corpus

    def load_embeddings(self) -> np.ndarray:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        embeddings_dir = os.path.join(project_root, "data", "embeddings")
        return np.load(os.path.join(embeddings_dir, "embeddings.npy"))

    def build_index(self):
        embeddings = self.load_embeddings()
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        return index

    def embed_text(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, padding=True, max_length=512
        )
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).detach().numpy()

    def retrieve(self, query: str, top_n: int = 3) -> List[str]:
        query_embedding = self.embed_text(query)
        distances, indices = self.index.search(query_embedding, top_n)
        corpus = self.load_processed_texts()
        return [corpus[i] for i in indices[0]]


# 示例用法
if __name__ == "__main__":
    rag_service = RAGService()
    query = "你的查询内容"
    results = rag_service.retrieve(query)
    for result in results:
        print(result)
