import re
words = re.findall(r'\w+', open('lion.docx').read().lower())
Counter(words)