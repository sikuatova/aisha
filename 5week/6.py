import re
def text_sub(text):
     patterns = '\s'
     x = re.sub('\s', '.', text)
     print(x)
text_sub("I go to school")