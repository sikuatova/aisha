import re
def text_find(text):
     patterns = '^[A-Z]?[a-z]*$'
     if re.findall(patterns,text):
          return 'OK'
     else:
          return "NO"
print(text_find('Abcd'))
print(text_find('aBcd'))