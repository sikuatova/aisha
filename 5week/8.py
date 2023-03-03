import re
def upper(text):
     patterns = '[A-Z][^A-Z]*'
     print(re.findall(patterns, text))
upper('IGoToSchool')