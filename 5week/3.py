import re
def text_search(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
	
print(text_search("aab_cbbbc"))
print(text_search("aab_Abbbc"))
print(text_search("Aaab_abbbc"))