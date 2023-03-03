
import re 

def match_string(text):
    patterns = r'^ab*?'
    if re.match(patterns, text):
        return 'good'
    else:
        return 'bad'
print(match_string("abbbb"))
print(match_string("sbbb"))
