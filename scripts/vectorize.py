import os
import numpy as np
from transformers import AutoTokenizer, AutoModel


def load_processed_texts(processed_dir):
    documents = []
    filenames = []
    for filename in os.listdir(processed_dir):
        if filename.endswith(".txt"):
            with open(
                os.path.join(processed_dir, filename), "r", encoding="utf-8"
            ) as file:
                documents.append(file.read())
                filenames.append(filename)
    print(f"Loaded {len(documents)} documents from {processed_dir}")
    return documents, filenames


def embed_texts(documents, model_name="models/bert-base-uncased"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    embeddings = []
    for i, doc in enumerate(documents):
        inputs = tokenizer(
            doc, return_tensors="pt", truncation=True, padding=True, max_length=512
        )
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()
        embeddings.append(embedding)
        print(f"Generated embedding for document {i+1}/{len(documents)}")
    return np.vstack(embeddings)


def save_embeddings(embeddings_dir, embeddings, filenames):
    if not os.path.exists(embeddings_dir):
        os.makedirs(embeddings_dir)
    for embedding, filename in zip(embeddings, filenames):
        basename = os.path.splitext(filename)[0]
        np.save(os.path.join(embeddings_dir, basename + ".npy"), embedding)
        print(f"Saved embedding for {filename} to {embeddings_dir}")


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    processed_dir = os.path.join(project_root, "data", "processed")
    embeddings_dir = os.path.join(project_root, "data", "embeddings")

    # 加载处理后的文本
    documents, filenames = load_processed_texts(processed_dir)

    # 生成嵌入向量
    embeddings = embed_texts(documents)

    # 保存嵌入向量
    save_embeddings(embeddings_dir, embeddings, filenames)


if __name__ == "__main__":
    main()
