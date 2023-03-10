a_string=input()

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(a_string))
    return a_string == reversed_string

print(palindrome(a_string))