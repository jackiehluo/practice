import re
import sys 

s = sys.stdin.read()

t = re.compile(r"""
(id="question-summary-(?P<id>\d+)")
(.*?)
(<h3><a\s*?href=".*?">(?P<subject>.*?)</a></h3>)
(.*?)
(<span\s+?title=".*?"\s+?class="relativetime"[^>]*>(?P<relativetime>.*?)</span>)
""",re.X|re.S)

for match in t.finditer(s):
    print ";".join([match.group("id"), match.group("subject"), match.group("relativetime")])
