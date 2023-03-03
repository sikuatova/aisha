import re

def match_text(text):
    patterns = r'^ab{2,3}?'
    if re.match(patterns, text):
        return 'alright'
    else:
        return 'try again'
print(match_text("ab"))
print(match_text("abbb"))