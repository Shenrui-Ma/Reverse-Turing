import os
from docx import Document


def load_docx_files(raw_dir):
    documents = []
    filenames = []
    for filename in os.listdir(raw_dir):
        if filename.endswith(".docx"):
            doc = Document(os.path.join(raw_dir, filename))
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            documents.append("\n".join(full_text))
            filenames.append(filename)
            print(f"Loaded document: {filename}")
    print(f"Total documents loaded: {len(documents)}")
    return documents, filenames


def save_processed_texts(processed_dir, documents, filenames):
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    for doc, filename in zip(documents, filenames):
        base_name = os.path.splitext(filename)[0]  # 去掉文件扩展名
        with open(
            os.path.join(processed_dir, f"{base_name}.txt"), "w", encoding="utf-8"
        ) as file:
            file.write(doc)
            print(f"Saved processed document: {base_name}.txt")
    print(f"Total documents saved: {len(documents)}")


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    raw_dir = os.path.join(project_root, "data", "raw")
    processed_dir = os.path.join(project_root, "data", "processed")

    # 加载和预处理docx文档
    documents, filenames = load_docx_files(raw_dir)
    save_processed_texts(processed_dir, documents, filenames)


if __name__ == "__main__":
    main()
