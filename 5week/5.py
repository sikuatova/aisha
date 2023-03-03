import re

def text_end(text):
     patterns = '^a(.)*b$'
     if re.match(patterns, text):
          return "Yup"
     else:
          return "Nope"
print(text_end('apppb'))
print(text_end('abba'))