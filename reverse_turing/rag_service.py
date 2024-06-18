import os
import numpy as np
import faiss
from transformers import AutoTokenizer, AutoModel
from typing import List

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


class RAGService:
    def __init__(self, model_name: str = "bert-base-chinese"):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        model_path = os.path.join(project_root, "models", model_name)
        # 调试
        print("Loading model from", model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModel.from_pretrained(model_path)
        self.index = self.build_index()

    def load_processed_texts(self) -> List[str]:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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
        # 嵌入模型路径在：F:\Repos\Reverse_Turing\data\embeddings
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        embeddings_dir = os.path.join(project_root, "data", "embeddings")

        # 初始化一个空列表来存储所有嵌入
        all_embeddings = []

        # 遍历embeddings目录下的所有文件
        for filename in os.listdir(embeddings_dir):
            if filename.endswith(".npy"):
                # 加载每个嵌入文件并添加到列表中
                embeddings_path = os.path.join(embeddings_dir, filename)
                embeddings = np.load(embeddings_path)
                all_embeddings.append(embeddings)

        # 将所有嵌入合并成一个NumPy数组
        if all_embeddings:
            all_embeddings = np.vstack(all_embeddings)
        else:
            all_embeddings = np.array([])  # 如果没有嵌入文件，返回空数组

        return all_embeddings

    def build_index(self):
        embeddings = self.load_embeddings()
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        return index

    def embed_text(self, text: str) -> np.ndarray:
        # 调试
        print("query text:", text, "Now embedding the query...")
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, padding=True, max_length=512
        )
        outputs = self.model(**inputs)
        print(outputs.last_hidden_state.shape)
        return outputs.last_hidden_state.mean(dim=1).detach().numpy()

    def retrieve(self, query: str, top_n: int = 1) -> List[str]:
        try:
            query_embedding = self.embed_text(query)

            # 搜索
            print("Now searching for the query...")
            distances, indices = self.index.search(query_embedding, top_n)

            # 取出文档内容
            print("Now retrieving the documents...")
            corpus = self.load_processed_texts()
            # print("corpus :", corpus)

            # 返回结果, 取top_n个
            print("Returning the results...")
            return str([corpus[i] for i in indices[0]])
        except Exception as e:
            print("Error in RAGService.retrieve:", str(e))
            raise


# # 示例用法
# if __name__ == "__main__":
#     rag_service = RAGService()
#     query = "你是谁？"
#     results = rag_service.retrieve(query)
#     print("retrieved results:")
#     for result in results:
#         print(result)
