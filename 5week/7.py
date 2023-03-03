import re
def to_CamelCase(text):
     return ''.join(x.capitalize() or '_' for x in text.split('_'))
print(to_CamelCase("snake_case_to_camel"))
