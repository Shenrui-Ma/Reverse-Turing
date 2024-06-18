# -*- coding: utf-8 -*-

import os
from volcenginesdkarkruntime import Ark
from dotenv import load_dotenv
# from scripts.character_settings import character_settings


def get_api_key_Doubao():
    load_dotenv()  # 加载环境变量
    api_key = os.getenv("API_KEY")
    model = os.getenv("MODEL_NAME")
    return api_key, model


def chat_with_Doubao(query, retrieved_docs):
    # 调试信息
    print("Initializing Doubao-Lite-4k chatbot...")
    client = Ark(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key=get_api_key_Doubao()[0],
    )

    print("Doubao-Lite-4k chatbot initialized.")

    # character_setting = character_settings.get(character, character_settings["default"])

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        # model="ep-20240610140329-rbnzb", # Doubao-lite-4k
        model=get_api_key_Doubao()[1],  # Doubao-pro-32k
        messages=[
            {
                "role": "system",
                "content": retrieved_docs,
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


# 测试
if __name__ == "__main__":
    query = "你好，请问有什么可以帮助您？"
    retrieved_docs = "你扮演米哈游旗下游戏《原神》的角色胡桃。"
    chat_with_Doubao(query, retrieved_docs)
