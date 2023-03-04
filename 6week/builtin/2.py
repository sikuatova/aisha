string=input()
def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print(uppercase_letter_count, lowercase_letter_count) 


count_upper_lower(string)
