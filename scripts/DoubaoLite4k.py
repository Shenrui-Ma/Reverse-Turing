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


        ],
        ],
