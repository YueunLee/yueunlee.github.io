import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

style_append = '''
body {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: sans-serif;
  line-height: 1.6;
}
#refs {
    counter-reset: ref-counter;
    list-style: none;
    padding-left: 0;
}
#refs li {
    counter-increment: ref-counter;
    margin-bottom: 0.5em;
    position: relative;
    padding-left: 2em;
}
#refs li::before {
    content: "[" counter(ref-counter) "] ";
    position: absolute;
    left: 0;
    color: #333;
    font-weight: bold;
}
'''

with open(filename, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. <style> 블럭 맨 끝에 CSS 추가
style_tag = soup.find('style')
if style_tag:
    style_tag.append('\n' + style_append)

# 2. <div id="refs"...> → <h2> + <ol> 구조로 변경 (같은 위치)
refs_div = soup.find("div", id="refs", class_="references")
if refs_div:
    entries = refs_div.find_all("div", class_="csl-entry")
    if entries:
        h2 = soup.new_tag("h2")
        h2.string = "References"
        ol = soup.new_tag("ol", id="refs")
        for entry in entries:
            li = soup.new_tag("li", id=entry.get("id"))
            li.append(BeautifulSoup(entry.decode_contents(), "html.parser"))
            ol.append(li)

        refs_div.clear()
        refs_div.append(h2)
        refs_div.append(ol)
        del refs_div["class"]
        del refs_div["role"]

# 저장
with open(filename, 'w', encoding='utf-8') as f:
    f.write(str(soup))
