import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

# 완전히 대체할 CSS 내용
new_style_content = '''
code{white-space: pre-wrap;}
span.smallcaps{font-variant: small-caps;}
div.columns{display: flex; gap: min(4vw, 1.5em);}
div.column{flex: auto; overflow-x: auto;}
div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
ul.task-list[class]{list-style: none;}
ul.task-list li input[type="checkbox"] {
    font-size: inherit;
    width: 0.8em;
    margin: 0 0.8em 0.2em -1.6em;
    vertical-align: middle;
}
/* CSS for citations */
div.csl-bib-body { }
div.csl-entry {
    clear: both;
    margin-bottom: 0em;
}
.hanging-indent div.csl-entry {
    margin-left:2em;
    text-indent:-2em;
}
div.csl-left-margin {
    min-width:2em;
    float:left;
}
div.csl-right-inline {
    margin-left:2em;
    padding-left:1em;
}
div.csl-indent {
    margin-left: 2em;
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
    style_tag.string = new_style_content

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
