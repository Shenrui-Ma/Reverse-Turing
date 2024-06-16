import os
import re
import json

RAW_DATA_DIR = "../data/raw/"
PROCESSED_DATA_DIR = "../data/processed/"


def preprocess_text(text):
    # 去除标点符号
    text = re.sub(r"[^\w\s]", "", text)
    # 转换为小写
    text = text.lower()
    return text


def preprocess_files():
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)

    for filename in os.listdir(RAW_DATA_DIR):
        if filename.endswith(".txt"):
            with open(
                os.path.join(RAW_DATA_DIR, filename), "r", encoding="utf-8"
            ) as file:
                text = file.read()
                processed_text = preprocess_text(text)
                processed_filename = os.path.join(PROCESSED_DATA_DIR, filename)
                with open(processed_filename, "w", encoding="utf-8") as processed_file:
                    processed_file.write(processed_text)
                print(f"Processed {filename} and saved to {processed_filename}")


if __name__ == "__main__":
    preprocess_files()
