# Reverse-Turingproject_root/
│
├── webui/                   # 前端应用
│   ├── public/
│   ├── src/
│   ├── pages/
│   ├── components/
│   ├── styles/
│   ├── package.json
│   └── next.config.js
│
├── backend/                 # 后端应用
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI 主应用入口
│   │   ├── dependencies.py  # 依赖管理
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py      # 聊天相关的路由
│   │   │   └── rag.py       # RAG 检索相关的路由
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── rag_service.py # RAG 检索服务
│   │   │   └── model_service.py # 大模型调用服务
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── chat_model.py # 聊天相关的数据模型
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── helpers.py   # 辅助函数
│   ├── data/
│   │   ├── raw/             # 原始文档
│   │   ├── processed/       # 处理后的文档
│   │   └── embeddings/      # 嵌入向量文件
│   ├── scripts/
│   │   ├── preprocess.py    # 预处理脚本
│   │   └── vectorize.py     # 向量化脚本
│   ├── tests/               # 测试代码
│   │   ├── __init__.py
│   │   ├── test_chat.py     # 聊天相关的测试
│   │   └── test_rag.py      # RAG 检索相关的测试
│   ├── requirements.txt     # Python 依赖包
│   └── README.md            # 项目说明
│
├── .gitignore
└── docker-compose.yml       # Docker Compose 配置文件
