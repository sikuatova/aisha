def polindrome(string):
    left = string[0:int(len(string) / 2)]
    right = string[int(len(string)/2 + 1):len(string)]
    if left[len(left)::-1] == right:
        print("IT IS POLINDROME") 
    else:
        print("IT IS NOT POLINDROME")
        
polindrome("ult")
polindrome("qazaq")