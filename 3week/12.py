def histogram(list):
    histo = ""
    for i in range(len(list)):
        if i == 0:
            histo += "*"*list[i]
        else:
            histo += "\n" + "*"*list[i]
    print(histo) 
    
histogram([4, 9, 7])