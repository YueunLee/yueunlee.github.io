#!/bin/bash

read -p "Enter the title for the HTML file: " TITLE
DATE=$(date +%F)

# 파일명으로 쓸 제목 가공 (대소문자 유지, 영문/숫자 외는 하이픈으로 변환)
FILENAME_TITLE=$(echo "$TITLE" | sed -E 's/[^a-zA-Z0-9]+/-/g' | sed -E 's/^-+|-+$//g')
OUTFILE="${DATE}-${FILENAME_TITLE}.html"

# JS 스크립트를 포함하는 파일 생성 (</body> 바로 전에 삽입)
cat <<'EOF' > script_footer.html
<script>
document.addEventListener("DOMContentLoaded", () => {
  const refs = Array.from(document.querySelectorAll('#refs li'));
  document.querySelectorAll('.citation').forEach(citation => {
    const citeId = citation.getAttribute('data-cites');
    if (!citeId) return;
    const refElem = document.getElementById('ref-' + citeId);
    if (!refElem) return;
    const index = refs.indexOf(refElem) + 1;
    if (index === 0) return;
    const a = document.createElement('a');
    a.href = '#ref-' + citeId;
    a.className = 'citation';
    a.textContent = `[${index}]`;
    citation.replaceWith(a);
  });
});
</script>
EOF

# pandoc 변환 (임시파일 생성)
pandoc main.tex --citeproc --bibliography=ref.bib --mathjax -s --include-after-body=script_footer.html -o temp_main.html

# <header> 태그 삭제
sed '/<header[^>]*>/,/<\/header>/d' temp_main.html > temp_noheader.html

# YAML 메타데이터 텍스트 생성
cat <<EOF > meta_block.txt
---
title: "$TITLE"
date: $DATE
---
EOF

# _posts 폴더에 최종 파일 생성
cat meta_block.txt temp_noheader.html > "_posts/$OUTFILE"

# 임시 파일 삭제
rm script_footer.html temp_main.html temp_noheader.html meta_block.txt

python fix.py "_posts/$OUTFILE"

echo "Generated file: _posts/$OUTFILE"
