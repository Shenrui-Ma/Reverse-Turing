import os
import numpy as np
from transformers import AutoTokenizer, AutoModel


def embed_texts(documents, model_name="models/bert-base-uncased"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    embeddings = []
    for doc in documents:
        inputs = tokenizer(
            doc, return_tensors="pt", truncation=True, padding=True, max_length=512
        )
        outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).detach().numpy())
    return np.vstack(embeddings)


def save_embeddings(embeddings_dir, embeddings):
    if not os.path.exists(embeddings_dir):
        os.makedirs(embeddings_dir)
    np.save(os.path.join(embeddings_dir, "embeddings.npy"), embeddings)
