#!/bin/bash

# 切换到脚本所在目录
cd "$(dirname "$0")"

# 激活 Conda 环境
source ./turenv/conda/etc/profile.d/conda.sh
conda activate ./turenv/env

# 运行 Python 脚本
python main.py

# 如果 Python 脚本执行失败,暂停
if [ $? -ne 0 ]; then
    echo "Press any key to continue..."
    read -n 1 -s
fi