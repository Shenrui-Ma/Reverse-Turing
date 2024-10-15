#!/bin/bash

# 设置工作目录为脚本所在目录
cd "$(dirname "$0")"

# 设置环境变量
export PATH="$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
export TMP="$PWD/turenv"
export TEMP="$PWD/turenv"

# 停用可能存在的conda环境
conda deactivate 2>/dev/null || true

# 设置安装目录
INSTALL_DIR="$PWD/turenv"
CONDA_ROOT_PREFIX="$PWD/turenv/conda"
INSTALL_ENV_DIR="$PWD/turenv/env"
NODEJS_DIR="$PWD/turenv/nodejs"
PIP_CMD="$PWD/turenv/env/bin/pip"
PYTHON_CMD="$PWD/turenv/env/bin/python"
MINICONDA_DOWNLOAD_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
NODEJS_DOWNLOAD_URL="https://nodejs.org/dist/v18.17.0/node-v18.17.0-linux-x64.tar.xz"

if ! command -v conda &> /dev/null; then
    echo "Downloading Miniconda..."
    mkdir -p "$INSTALL_DIR/conda"
    wget -O "$INSTALL_DIR/conda/miniconda_installer.sh" "$MINICONDA_DOWNLOAD_URL"
    
    if [ $? -ne 0 ]; then
        echo "Failed to download Miniconda."
        exit 1
    fi
    
    bash "$INSTALL_DIR/conda/miniconda_installer.sh" -b -p "$CONDA_ROOT_PREFIX"
    
    if [ $? -ne 0 ]; then
        echo "Cannot install Miniconda."
        exit 1
    else
        echo "Miniconda installed successfully."
    fi
    
    rm "$INSTALL_DIR/conda/miniconda_installer.sh"
fi

if [ ! -d "$INSTALL_ENV_DIR" ]; then
    echo "Creating Conda Environment..."
    "$CONDA_ROOT_PREFIX/bin/conda" create --no-shortcuts -y -k --prefix "$INSTALL_ENV_DIR" python=3.8
    
    if [ $? -ne 0 ]; then
        echo "Failed to Create Environment."
        exit 1
    fi
fi

source "$CONDA_ROOT_PREFIX/bin/activate" "$INSTALL_ENV_DIR"

if [ $? -ne 0 ]; then
    echo "Failed to activate Env."
    exit 1
else
    echo "Successfully created and activated env."
fi

echo "Installing required packages..."
"$PIP_CMD" install fastapi requests pydantic uvicorn pillow nltk websocket-client python-dotenv numpy python-docx transformers faiss-cpu torch volcengine-python-sdk[ark]

if [ $? -ne 0 ]; then
    echo "Failed to install packages."
    exit 1
else
    echo "Successfully installed all packages."
fi

echo "Setting up Node.js and npm..."
wget -O nodejs.tar.xz "$NODEJS_DOWNLOAD_URL"
tar -xJf nodejs.tar.xz -C "$INSTALL_DIR"
mv "$INSTALL_DIR/node-v18.17.0-linux-x64" "$NODEJS_DIR"
rm nodejs.tar.xz

export PATH="$PATH:$NODEJS_DIR/bin"

cd webui
npm install

if [ $? -ne 0 ]; then
    echo "Failed to install project dependencies."
    exit 1
else
    echo "Successfully installed project dependencies."
fi

npm install -g pnpm

if [ $? -ne 0 ]; then
    echo "Failed to install pnpm."
    exit 1
else
    echo "Successfully installed pnpm."
fi

pnpm install

if [ $? -ne 0 ]; then
    echo "Failed to install node_modules."
    exit 1
else
    echo "Successfully installed node_modules."
fi

echo "Environment setup complete."