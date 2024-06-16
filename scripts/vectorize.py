import os
import numpy as np
from utils import embed_texts, save_embeddings


def load_processed_texts(processed_dir):
    documents = []
    for filename in os.listdir(processed_dir):
        if filename.endswith(".txt"):
            with open(
                os.path.join(processed_dir, filename), "r", encoding="utf-8"
            ) as file:
                documents.append(file.read())
    return documents


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    processed_dir = os.path.join(project_root, "data", "processed")
    embeddings_dir = os.path.join(project_root, "data", "embeddings")

    # 加载处理后的文本
    documents = load_processed_texts(processed_dir)

    # 生成嵌入向量
    embeddings = embed_texts(documents)

    # 保存嵌入向量
    save_embeddings(embeddings_dir, embeddings)


if __name__ == "__main__":
    main()
