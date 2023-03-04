string=input()
def polindrome(string):
    revstring=string[::-1]
    if string==revstring:
        print("string is palindrome")
    else:
        print("not")

polindrome(string) 
