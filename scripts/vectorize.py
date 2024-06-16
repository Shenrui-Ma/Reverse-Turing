import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

PROCESSED_DATA_DIR = "../data/processed/"
EMBEDDINGS_DATA_DIR = "../data/embeddings/"


def vectorize_texts(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors.toarray(), vectorizer


def vectorize_files():
    if not os.path.exists(EMBEDDINGS_DATA_DIR):
        os.makedirs(EMBEDDINGS_DATA_DIR)

    texts = []
    filenames = []

    for filename in os.listdir(PROCESSED_DATA_DIR):
        if filename.endswith(".txt"):
            with open(
                os.path.join(PROCESSED_DATA_DIR, filename), "r", encoding="utf-8"
            ) as file:
                text = file.read()
                texts.append(text)
                filenames.append(filename)

    vectors, vectorizer = vectorize_texts(texts)

    for i, filename in enumerate(filenames):
        embedding_filename = os.path.join(
            EMBEDDINGS_DATA_DIR, filename.replace(".txt", ".npy")
        )
        np.save(embedding_filename, vectors[i])
        print(f"Vectorized {filename} and saved to {embedding_filename}")

    # 保存TF-IDF向量器以便后续使用
    with open(
        os.path.join(EMBEDDINGS_DATA_DIR, "vectorizer.json"), "w", encoding="utf-8"
    ) as vectorizer_file:
        json.dump(vectorizer.vocabulary_, vectorizer_file)
    print("Saved TF-IDF vectorizer vocabulary to vectorizer.json")


if __name__ == "__main__":
    vectorize_files()
