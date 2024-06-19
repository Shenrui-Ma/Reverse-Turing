import re
from bs4 import BeautifulSoup


text = """<a name="角色形象">你好我是你爹</div><span></h3>"""
soup = BeautifulSoup(text, "html.parser")
section_anchor = soup.find("a", {"name": "角色形象"})

content = []
for sibling in section_anchor.next_siblings:
    if sibling.name == "span" and sibling.get("data-text") == "true":
        break
    if sibling.name == "div" and sibling.get("class") == ["para"]:
        content.append(sibling.get_text(strip=True))
print(content)
