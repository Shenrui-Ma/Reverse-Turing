import os
import re
import requests
from bs4 import BeautifulSoup


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save_content(file_path, title, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{title}\n{content}")


def clean_text(text):
    # 去掉所有<>括起来的标签和[]括起来的数字
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[\d+\]", "", text)
    return text


def scrape_baidu_baike(url, character_name):
    base_dir = os.path.join(os.getcwd(), "data", "raw", character_name)
    create_directory(base_dir)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # 调试代码，打印该页面的前500个字符
    print(soup.prettify()[:500])
    # 把所有的内容先写入"F:\Repos\Reverse_Turing\data\processed\Arlecchino\temp.txt"
    with open(
        r"F:\Repos\Reverse_Turing\data\processed\Arlecchino\temp.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(soup.prettify())

    sections = {
        "角色形象": "image.txt",
        "角色生活": "life.txt",
        "角色能力": "ability.txt",
        "角色经历": "experience.txt",
        "人际关系": "relationship.txt",
        "角色评价": "comment.txt",
    }

    for section_title, file_name in sections.items():
        section_anchor = soup.find("a", {"name": section_title})
        if section_anchor is None:
            continue  # 如果没有找到对应的小标题，跳过当前循环
        print(f"Scraping {section_title}...")

        content = []
        capture = False
        span_content = ""
        for sibling in section_anchor.next_siblings:
            if sibling.name == "span" and sibling.get("data-text") == "true":
                capture = True
                span_content = sibling.get_text(strip=True)
                continue
            if capture:
                if sibling.name == "div" and sibling.get("class") == [
                    "para_kAVYT content_Fwuml MARK_MODULE"
                ]:
                    content.append(span_content)
                    content.append(sibling.get_text(strip=True))
                    break
                content.append(sibling.get_text(strip=True))
        print(content)

        cleaned_content = clean_text(" ".join(content))
        print(f"Cleaned content: {cleaned_content}")

        # file_path = os.path.join(base_dir, file_name)
        file_path = os.path.join(
            "F:\\Repos\\Reverse_Turing\\data\\raw\\Arlecchino", file_name
        )
        save_content(file_path, section_title, cleaned_content)


if __name__ == "__main__":
    url = "https://baike.baidu.com/item/%E9%98%BF%E8%95%BE%E5%A5%87%E8%AF%BA/61716404?fr=ge_ala"
    character_name = "Arlecchino"  # 替换为你要爬取的角色名
    scrape_baidu_baike(url, character_name)
