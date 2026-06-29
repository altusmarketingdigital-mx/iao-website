import fitz
doc = fitz.open('checklist.pdf')
text = ''.join([p.get_text() for p in doc])
print("-----EXTRACTED TEXT START-----")
print(text)
print("-----EXTRACTED TEXT END-----")
