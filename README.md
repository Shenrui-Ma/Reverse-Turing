# Reverse Turing

<div>
English | [简体中文](README-zh.md)  <br>
<a target="_blank" href="https://space.bilibili.com/12595237?spm_id_from=333.1007.0.0">
<img alt="bilibili_acount" src="webui\public\images\bilibili_acount.png" style="width: 150px;"/>
 <p style="font-size: 14px; color: #333;">Contact me: <a href="mailto:yapuhu042228@163.com" style="color: #0066cc;">yapuhu042228@163.com</a> or <a href="mailto:shenruima@gmail.com" style="color: #0066cc;">shenruima@gmail.com</a></p>
</a>
</div>

## Disclaimer / 免责声明

I do not hold any responsibility for any illegal usage of the codebase. Please refer to your local laws about DMCA and other related laws.  
我不对代码库的任何非法使用承担任何责任. 请参阅您当地关于 DMCA (数字千年法案) 和其他相关法律法规.

## Quick Start / 快速开始

Users attempt to mimic the language habits of LLMs as closely as possible, concealing their human identity, and persist in maintaining this facade for as many rounds as possible without being discovered. Users, along with other chatbots connected to ByteDance's Douyin large language model, participate as characters. In each round, a random question is generated. The user and other chatbots each provide their own answers to this question, and then collectively vote on who seems most human-like.
用户尽可能模仿 LLM 的语言习惯，隐藏人类身份，坚持尽可能多轮次不被发现。用户与其他接入字节豆包大模型的聊天机器人作为参与角色，每回合随机生成一个问题，用户与其他机器人就该问题各自给出自己的回答，并一起投票谁最像人类。

## Usage / 使用

### Windows Installation / Windows 安装

```
git clone https://github.com/Shenrui-Ma/Reverse-Turing.git
cd Reverse-Turing

.\install_env.bat

conda activate .\turenv\env

pip install -r requirements.txt

```

Run in the root directory / 在根目录下运行

```
./start.sh
```

### Linux Installation / Linux 安装

```
git clone https://github.com/Shenrui-Ma/Reverse-Turing.git
cd Reverse-Turing

chmod +x install_env.sh
./install_env.sh

source ./turenv/conda/etc/profile.d/conda.sh
conda activate ./turenv/env

pip install -r requirements.txt

```

Run in the root directory / 在根目录下运行

```
./start.sh
```

## Note / 说明

The program now integrates my personal ByteDance Doubao-pro-128k model API, but I'm unsure how long it will be available. If you want to use your own API, you can create a new .env file in the root directory and add the line API_KEY=<your API_KEY>.

If you want to have voice effects, you need to run the GPT-Sovits project yourself. You only need to change the corresponding port number.

1.现在程序集成了本人的字节 Doubao-pro-128k 模型 API,不知道能用多久。如果要使用自己的，可以在根目录新建一个.env 文件，并写入 API_KEY=<你的 API_KEY>。

2.如果想要有配音效果，需要自行运行的 GPT-Sovits 项目，你只需要更改成对应的端口号

## Credits / 鸣谢

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
